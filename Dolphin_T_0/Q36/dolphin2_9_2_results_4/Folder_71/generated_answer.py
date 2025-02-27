def filter_chars(s):
    off_limits = [chr(c) for c in range(ord('*'), ord('['))]
    for i in range(82, 89):
        if s[i] in off_limits:
            s = ''.join([c for c in s if c != s[i]])
    return s