from collections import Counter

def palindromes_between_indices(s):
    if len(s) < 9:
        return set()
    substring = s[7:9].lower()
    char_count = Counter(filter(str.isalpha, substring))

    def can_form_palindrome(counts):
        odd_count = sum((1 for count in counts.values() if count % 2 != 0))
        return odd_count <= 1

    def generate_palindromes(half, middle, length):
        if len(half) == length // 2:
            yield (half + middle + half[::-1])
        else:
            for char in char_count:
                if char_count[char] > 0:
                    char_count[char] -= 2
                    yield from generate_palindromes(half + char, middle, length)
                    char_count[char] += 2
    palindromes = set()
    if can_form_palindrome(char_count):
        middle = ''
        for char in char_count:
            if char_count[char] % 2 != 0:
                middle = char
                break
        for length in range(3, len(substring) + 1):
            palindromes.update(generate_palindromes('', middle, length))
    return palindromes