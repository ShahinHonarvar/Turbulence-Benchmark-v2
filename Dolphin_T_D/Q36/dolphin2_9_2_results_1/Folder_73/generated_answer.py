def filter_chars(s):
    toremove = [s[i] for i in range(66, 90) if s[i] > '#' and s[i] < 'T']
    for c in toremove:
        s = s.replace(c, '')
    return s