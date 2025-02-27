def filter_chars(s):
    for c in range(46, 68):
        if s[c] > 'H' and s[c] < 's':
            return s[:c] + s[c + 1:]
    return s