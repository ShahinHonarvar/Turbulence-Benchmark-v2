def palindromes_of_specific_lengths(s):

    def is_palindrome(substr):
        return substr.lower() == substr.lower()[::-1]

    def is_letters_only(substr):
        return substr.isalpha()
    palindrome_set = set()
    for length in range(39, 53):
        for start in range(16, 95 - length + 1):
            substr = s[start:start + length]
            if is_palindrome(substr) and is_letters_only(substr):
                palindrome_set.add(substr.lower())
    return palindrome_set