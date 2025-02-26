def palindromes_of_specific_lengths(s):

    def is_palindrome(substr):
        return substr.lower() == substr.lower()[::-1]

    def is_letters_only(substr):
        return substr.isalpha()
    palindromes = set()
    for length in range(10, 21):
        for start in range(10, 76 - length + 1):
            substr = s[start:start + length]
            if is_palindrome(substr) and is_letters_only(substr):
                palindromes.add(substr.lower())
    return palindromes