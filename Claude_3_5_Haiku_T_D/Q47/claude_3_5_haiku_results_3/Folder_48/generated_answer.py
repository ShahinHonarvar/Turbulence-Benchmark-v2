def palindromes_of_specific_lengths(s):

    def is_palindrome(substr):
        return substr.lower() == substr.lower()[::-1]

    def is_letter_only(substr):
        return substr.isalpha()
    palindromes = set()
    for length in range(104, 121):
        for start in range(155, 284 - length + 1):
            substr = s[start:start + length]
            if is_palindrome(substr) and is_letter_only(substr):
                palindromes.add(substr)
    return palindromes