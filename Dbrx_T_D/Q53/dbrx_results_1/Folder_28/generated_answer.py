def is_palindrome(s):
    s = ''.join((c.lower() for c in s if c.isalpha()))
    return s == s[::-1]

def palindrome_of_length_at_least_n(s, n=42):
    palindromes = {s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1) if is_palindrome(s[i:j]) and len(s[i:j]) >= n}
    return palindromes