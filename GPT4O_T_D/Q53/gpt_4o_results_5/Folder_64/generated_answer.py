def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    palindromes = set()
    normalized_s = ''.join([c.lower() for c in s if c.isalpha()])
    n = len(normalized_s)
    for start in range(n):
        for end in range(start + 9, n + 1):
            substr = normalized_s[start:end]
            if is_palindrome(substr):
                palindromes.add(substr)
    return palindromes