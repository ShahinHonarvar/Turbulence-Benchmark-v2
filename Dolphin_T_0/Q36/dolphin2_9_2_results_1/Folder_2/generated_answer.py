def filter_chars(s):
    for c in range(421, 854):
        if 'D' < s[c] < 'J':
            s = s[:c] + s[c + 1:]
    return s