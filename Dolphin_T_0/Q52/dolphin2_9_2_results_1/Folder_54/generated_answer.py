def palindrome_of_length_n(s):
    s = ''.join((ch.lower() for ch in s if ch.isalpha()))
    n = 85
    return {s[i:i + n] for i in range(len(s) - n + 1) if s[i:i + n] == s[i:i + n][::-1] and len(s[i:i + n]) == n}