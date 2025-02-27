from collections import Counter

def palindromes_between_indices(s):
    if len(s) < 9:
        return set()
    s_segment = s[3:9].lower()

    def is_possible_palindrome(counter, length):
        odd_count = sum((1 for count in counter.values() if count % 2 != 0))
        if length % 2 == 0:
            return odd_count == 0
        else:
            return odd_count <= 1

    def generate_half_palindrome(current, counter, half_length, palindromes):
        if len(current) == half_length:
            full_palindrome = current + current[::-1]
            if len(full_palindrome) >= 4:
                palindromes.add(full_palindrome)
            if len(current) > 0 and len(current) < half_length:
                full_palindrome = current + current[-2::-1]
                if len(full_palindrome) >= 4:
                    palindromes.add(full_palindrome)
            return
        for char in sorted(counter.keys()):
            if counter[char] > 0:
                counter[char] -= 2
                generate_half_palindrome(current + char, counter, half_length, palindromes)
                counter[char] += 2
    letters = [c for c in s_segment if c.isalpha()]
    counter = Counter(letters)
    max_length = len(letters)
    results = set()
    for length in range(4, max_length + 1):
        if is_possible_palindrome(counter, length):
            generate_half_palindrome('', counter, length // 2, results)
    return results