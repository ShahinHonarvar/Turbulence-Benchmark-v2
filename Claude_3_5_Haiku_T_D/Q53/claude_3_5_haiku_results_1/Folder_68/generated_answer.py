def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()

    def is_palindrome(substr):
        return substr == substr[::-1] and substr.isalpha()
    for length in range(21, len(s) + 1):
        for start in range(len(s) - length + 1):
            substr = s[start:start + length]
            if is_palindrome(substr):
                palindromes.add(substr)
    return palindromes