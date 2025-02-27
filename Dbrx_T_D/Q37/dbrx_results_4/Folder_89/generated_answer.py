def filter_chars(s):
    for i in range(len(s)):
        if s[i] >= '!' and s[i] <= '@' and (i >= 11) and (i <= 32):
            s = s[:i] + s[i + 1:]
    return s