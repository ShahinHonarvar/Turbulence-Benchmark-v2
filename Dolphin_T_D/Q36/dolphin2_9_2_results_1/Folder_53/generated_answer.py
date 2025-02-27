def filter_chars(s):
    for c in range(90, 97):
        if s[c] > 'j' and s[c] < 'w':
            s = s.replace(s[c], '')
    return s