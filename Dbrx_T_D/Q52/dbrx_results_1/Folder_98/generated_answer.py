def palindrome_of_length_n(s):
    s = ''.join((c.lower() for c in s if c.isalpha()))
    n = 6
    return {s[i:j] for i in range(len(s)) for j in range(i + n, min(i + 2 * n, len(s) + 1)) if s[i:j] == s[i:j][::-1]}