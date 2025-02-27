from collections import Counter

def palindromes_between_indices(s):
    if len(s) < 9:
        return set()
    sub_str = s[6:9].lower()
    counter = Counter(filter(str.isalpha, sub_str))

    def can_form_palindrome(ctr):
        odd_count = sum((1 for count in ctr.values() if count % 2 != 0))
        return odd_count <= 1
    if not can_form_palindrome(counter):
        return set()

    def generate_palindromes(ctr, half_str=''):
        if all((count == 0 for count in ctr.values())):
            mid = half_str[::-1]
            return {half_str + mid} if len(half_str) > 1 else set()
        results = set()
        for char in list(ctr):
            if ctr[char] > 1:
                ctr[char] -= 2
                results.update(generate_palindromes(ctr, half_str + char))
                ctr[char] += 2
            elif ctr[char] == 1:
                if half_str or any((v > 1 for v in ctr.values())):
                    mid = half_str[::-1] + char
                    results.add(half_str + mid)
        return results
    return {palindrome for palindrome in generate_palindromes(counter) if len(palindrome) >= 3}