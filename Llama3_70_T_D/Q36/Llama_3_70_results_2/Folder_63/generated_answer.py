def filter_chars(s):
    orig = s
    for i in range(26, 80):
        if s[i] > '<' and s[i] < '>':
            orig = orig.replace(s[i], '')
    return orig