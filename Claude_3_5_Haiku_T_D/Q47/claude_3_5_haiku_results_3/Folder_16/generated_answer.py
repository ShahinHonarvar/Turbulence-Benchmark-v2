def palindromes_of_specific_lengths(s):

    def is_palindrome(substr):
        return substr.lower() == substr.lower()[::-1]

    def is_only_letters(substr):
        return substr.isalpha()
    palindromes = set()
    for start in range(15, 87 - 50):
        for length in range(51, 61):
            substr = s[start:start + length]
            if len(substr) == length and is_palindrome(substr) and is_only_letters(substr):
                palindromes.add(substr)
    return palindromes