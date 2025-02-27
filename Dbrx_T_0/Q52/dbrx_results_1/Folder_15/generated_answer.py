def palindrome_of_length_n(s):
    s = ''.join((c.lower() for c in s if c.isalpha()))
    return {s[i:j] for i in range(len(s)) for j in range(i + 1, min(i + 4, len(s) + 1)) if s[i:j] == s[i:j][::-1]}