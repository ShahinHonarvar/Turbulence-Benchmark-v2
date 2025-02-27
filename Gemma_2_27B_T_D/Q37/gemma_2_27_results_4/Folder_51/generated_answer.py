def filter_chars(s):
    for i in range(36, 41):
        if len(s) > i and 'H' <= s[i] <= 'e':
            s = s.replace(s[i], '')
    return s