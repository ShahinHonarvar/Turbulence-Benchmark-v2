def is_palindrome(s):
    return s.lower() == s[::-1].lower()

def palindrome_of_length_at_least_n(s):
    s = ''.join((c.lower() for c in s if c.isalpha()))
    palindromes = set()
    n = len(s)
    for i in range(n):
        for j in range(i + 13, n):
            if is_palindrome(s[i:j + 1]):
                palindromes.add(s[i:j + 1])
    return palindromes