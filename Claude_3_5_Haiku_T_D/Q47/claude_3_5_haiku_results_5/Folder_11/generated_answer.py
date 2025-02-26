def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word == word[::-1]

    def is_alphabetic(word):
        return word.isalpha()
    result = set()
    s = s.lower()
    for length in range(10, 37):
        for start in range(24, 98 - length + 1):
            substring = s[start:start + length]
            if is_palindrome(substring) and is_alphabetic(substring):
                result.add(substring)
    return result