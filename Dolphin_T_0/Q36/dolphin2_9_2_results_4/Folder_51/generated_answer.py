def filter_chars(s):
    replace = []
    for i in range(58, 81):
        if '5' < s[i] < '>':
            replace.append(s[i])
    for r in replace:
        s = s.replace(r, '')
    return s