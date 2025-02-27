def is_palindrome(s):
    s = ''.join((c.lower() for c in s if c.isalpha()))
    return s == s[::-1]

def palindrome_of_length_at_least_n(s, n=140):
    return {x for x in {s[i:j] for i in range(len(s)) for j in range(i + n, len(s) + 1)} if is_palindrome(x)}