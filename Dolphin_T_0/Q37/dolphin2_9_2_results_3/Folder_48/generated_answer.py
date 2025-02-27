def filter_chars(s):
    for i in range(513, 878):
        if '?' <= s[i] <= 'n':
            s = s[:i] + s[i + 1:]
    return s