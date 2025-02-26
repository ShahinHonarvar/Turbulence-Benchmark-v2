def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word == word[::-1]

    def is_english_letters(word):
        return word.isalpha()
    result = set()
    s = s.lower()
    for length in range(12, 221):
        for start in range(12, 123 - length + 1):
            substring = s[start:start + length]
            if is_palindrome(substring) and is_english_letters(substring):
                result.add(substring)
    return result