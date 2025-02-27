def filter_chars(s):
    for i in range(58, 82):
        if i < len(s) and 'F' < s[i] < 'O':
            c = s[i]
            s = s.replace(c, '')
    return s