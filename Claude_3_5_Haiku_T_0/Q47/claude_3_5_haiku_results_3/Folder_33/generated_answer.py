def palindromes_of_specific_lengths(s):

    def is_palindrome(substr):
        return substr.lower() == substr.lower()[::-1]

    def is_only_letters(substr):
        return substr.isalpha()
    palindromes = set()
    for length in range(103, 159):
        for start in range(130, 296 - length + 1):
            substr = s[start:start + length]
            if is_palindrome(substr) and is_only_letters(substr):
                palindromes.add(substr)
    return palindromes