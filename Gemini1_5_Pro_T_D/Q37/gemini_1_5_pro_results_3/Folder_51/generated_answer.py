def filter_chars(s):
    for i in range(36, 41):
        if i < len(s) and 'H' <= s[i] <= 'e':
            c = s[i]
            s = s.replace(c, '')
    return s