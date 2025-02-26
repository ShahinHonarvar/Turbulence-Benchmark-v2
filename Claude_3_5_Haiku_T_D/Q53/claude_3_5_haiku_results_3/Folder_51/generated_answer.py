def palindrome_of_length_at_least_n(s):

    def is_palindrome(substr):
        return substr.lower() == substr.lower()[::-1]
    n = 63
    palindromes = set()
    s = s.lower()
    for i in range(len(s)):
        for j in range(i + n, len(s) + 1):
            substr = s[i:j]
            if len(substr) >= n and all((c.isalpha() for c in substr)) and is_palindrome(substr):
                palindromes.add(substr)
    return palindromes