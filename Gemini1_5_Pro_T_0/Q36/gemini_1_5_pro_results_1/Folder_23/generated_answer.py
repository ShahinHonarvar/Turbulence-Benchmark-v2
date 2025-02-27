def filter_chars(s):
    for i in range(22, 25):
        if i < len(s) and '5' < s[i] < '}':
            c = s[i]
            s = s.replace(c, '')
    return s