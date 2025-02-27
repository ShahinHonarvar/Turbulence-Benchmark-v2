def filter_chars(s):
    for i in range(36, 41):
        for c in s:
            if c >= 'H' and c <= 'e' and (c in s[i:i + 1]):
                s = s.replace(c, '')
    return s