def palindrome_of_length_at_least_n(s):

    def is_palindrome(substr):
        return substr == substr[::-1]

    def is_only_letters(substr):
        return substr.isalpha()
    s = s.lower()
    palindromes = set()
    for length in range(92, len(s) + 1):
        for start in range(len(s) - length + 1):
            substr = s[start:start + length]
            if is_palindrome(substr) and is_only_letters(substr):
                palindromes.add(substr)
    return palindromes