def palindromes_of_specific_lengths(s):

    def is_palindrome(substr):
        return substr.lower() == substr.lower()[::-1]

    def is_only_letters(substr):
        return substr.isalpha()
    result = set()
    for length in range(26, 32):
        for start in range(33, 86 - length + 1):
            substr = s[start:start + length]
            if is_palindrome(substr) and is_only_letters(substr):
                result.add(substr)
    return result