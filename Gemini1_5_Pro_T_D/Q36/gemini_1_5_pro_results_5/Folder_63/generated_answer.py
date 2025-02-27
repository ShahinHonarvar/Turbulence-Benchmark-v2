def filter_chars(s):
    for i in range(26, 80):
        if i < len(s) and s[i] > '<' and (s[i] < '>'):
            c = s[i]
            s = s.replace(c, '')
    return s