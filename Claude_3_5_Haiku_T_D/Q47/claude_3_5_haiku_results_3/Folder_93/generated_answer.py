def palindromes_of_specific_lengths(s):

    def is_palindrome(substr):
        return substr.lower() == substr.lower()[::-1]

    def is_alphabetic(substr):
        return substr.isalpha()
    palindromes = set()
    for length in range(13, 50):
        for start in range(17, 96 - length + 1):
            substring = s[start:start + length]
            if is_palindrome(substring) and is_alphabetic(substring):
                palindromes.add(substring.lower())
    return palindromes