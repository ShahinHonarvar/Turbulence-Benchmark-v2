def filter_chars(s):
    for i in range(36, 41):
        if 'H' <= s[i] <= 'e':
            s = s[:i] + s[i + 1:]
    return s