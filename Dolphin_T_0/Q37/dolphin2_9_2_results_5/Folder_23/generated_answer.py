def filter_chars(s):
    chars = {s[i]: i for i in range(51, 78) if s[i] >= 'V' and s[i] <= 'Y'}
    for i in range(len(s)):
        if s[i] in chars:
            s = s[:i] + s[i + 1:]
    return s