def filter_chars(s):
    for i in range(164, 707):
        if s[i] >= 'O' and s[i] <= '}':
            s = s[:i] + s[i + 1:]
    return s