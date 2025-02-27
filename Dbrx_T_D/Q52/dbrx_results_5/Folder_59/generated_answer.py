def palindrome_of_length_n(s):
    s = ''.join((c.lower() for c in s if c.isalpha()))
    n = 39
    if n > len(s) or n < 1:
        return set()
    return {s[i:j] for i in range(len(s)) for j in range(i + 1, min(i + n + 1, len(s) + 1)) if s[i:j] == s[i:j][::-1]}