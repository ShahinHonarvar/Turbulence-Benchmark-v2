def filter_chars(s):
    for c in range(63, 89):
        if '*' < s[c] < 'w':
            s = s.replace(s[c], '')
    return s