def filter_chars(s):
    for i in range(min(225, len(s)), min(382, len(s))):
        if 'D' <= s[i] <= 'Y':
            s = s[:i] + s[i + 1:]
    return s