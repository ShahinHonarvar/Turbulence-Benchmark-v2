from collections import Counter

def palindromes_between_indices(s):
    if len(s) < 10:
        return set()
    substring = s[8:10].lower()
    char_count = Counter(filter(str.isalpha, substring))
    palindromes = set()

    def can_form_palindrome(counter):
        odd_count = sum((1 for count in counter.values() if count % 2 != 0))
        return odd_count <= 1

    def generate_palindromes(half, middle, counter):
        if len(half) * 2 + len(middle) >= 3:
            palindromes.add(half + middle + half[::-1])
        for char in list(counter.keys()):
            if counter[char] > 1:
                counter[char] -= 2
                generate_palindromes(half + char, middle, counter)
                counter[char] += 2
            elif counter[char] == 1 and (not middle):
                counter[char] -= 1
                generate_palindromes(half, char, counter)
                counter[char] += 1
    if can_form_palindrome(char_count):
        generate_palindromes('', '', char_count)
    return palindromes