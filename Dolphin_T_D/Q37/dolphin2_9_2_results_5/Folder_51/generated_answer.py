def filter_chars(s):
    for i in range(36, 41):
        if i in s and s[i] >= 'H' and (s[i] <= 'e'):
            s = s.replace(s[i], '')
    return s