def palindrome_of_length_at_least_n(s):

    def is_palindrome(s):
        return s.lower() == s[::-1].lower()
    n = 25
    s = ''.join((c for c in s if c.isalpha()))
    palindromes = set()
    for i in range(len(s) - n + 1):
        for j in range(i + n, len(s) + 1):
            if is_palindrome(s[i:j]):
                palindromes.add(s[i:j])
    return palindromes