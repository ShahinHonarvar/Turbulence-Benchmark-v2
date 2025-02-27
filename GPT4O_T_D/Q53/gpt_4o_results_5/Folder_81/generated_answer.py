def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = ''.join((c.lower() for c in s if c.isalpha()))
    palindromes = set()
    n = len(s)
    for start in range(n):
        for end in range(start + 33, n + 1):
            substring = s[start:end]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes