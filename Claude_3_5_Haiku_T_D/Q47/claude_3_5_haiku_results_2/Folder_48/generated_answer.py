def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word == word[::-1]

    def is_english_letters(word):
        return word.isalpha()
    result = set()
    for length in range(104, 121):
        for start in range(155, 284 - length + 1):
            substring = s[start:start + length].lower()
            if is_palindrome(substring) and is_english_letters(substring):
                result.add(substring)
    return result