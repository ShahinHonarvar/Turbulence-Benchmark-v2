def palindromes_of_specific_lengths(s):

    def is_palindrome(substr):
        return substr.lower() == substr.lower()[::-1]

    def is_alphabetic(substr):
        return substr.isalpha()
    palindromes = set()
    for length in range(24, 53):
        for start in range(10, 71 - length + 1):
            substr = s[start:start + length]
            if is_palindrome(substr) and is_alphabetic(substr):
                palindromes.add(substr)
    return palindromes