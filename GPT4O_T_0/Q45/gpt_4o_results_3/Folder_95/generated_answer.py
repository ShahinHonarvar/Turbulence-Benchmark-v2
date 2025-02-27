from collections import Counter

def palindromes_between_indices(s):
    if len(s) < 9:
        return set()
    substring = s[7:9].lower()

    def can_form_palindrome(counter):
        odd_count = sum((1 for count in counter.values() if count % 2 != 0))
        return odd_count <= 1

    def generate_palindromes(counter, half, odd_char, length):
        if len(half) == length // 2:
            if odd_char:
                yield (half + odd_char + half[::-1])
            else:
                yield (half + half[::-1])
            return
        for char in counter:
            if counter[char] > 0:
                counter[char] -= 2
                yield from generate_palindromes(counter, half + char, odd_char, length)
                counter[char] += 2
    counter = Counter(filter(str.isalpha, substring))
    if not can_form_palindrome(counter):
        return set()
    palindromes = set()
    for length in range(3, len(substring) + 1):
        for char in counter:
            if counter[char] % 2 != 0:
                counter[char] -= 1
                palindromes.update(generate_palindromes(counter, '', char, length))
                counter[char] += 1
        palindromes.update(generate_palindromes(counter, '', '', length))
    return palindromes