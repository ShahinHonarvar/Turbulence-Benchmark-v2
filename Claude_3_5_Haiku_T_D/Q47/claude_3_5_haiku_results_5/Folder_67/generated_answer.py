def palindromes_of_specific_lengths(s):

    def is_palindrome(substr):
        return substr.lower() == substr.lower()[::-1]

    def is_only_letters(substr):
        return substr.isalpha()
    palindromes = set()
    substring = s[65:100]
    for length in range(26, 34):
        for start in range(len(substring) - length + 1):
            substr = substring[start:start + length]
            if is_palindrome(substr) and is_only_letters(substr):
                palindromes.add(substr.lower())
    return palindromes