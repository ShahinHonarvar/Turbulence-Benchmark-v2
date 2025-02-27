def filter_chars(s):
    for c in range(163, 658):
        if s[c] > '(' and s[c] < ']':
            s = s.replace(s[c], '')
    return s