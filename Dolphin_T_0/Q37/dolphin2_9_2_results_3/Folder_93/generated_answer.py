def filter_chars(s):
    for i in range(38, 70):
        if s[i] >= 'H' and s[i] <= 'e':
            s = s[:i] + s[i + 1:]
    return s