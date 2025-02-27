def filter_chars(s):
    for i in range(45, 57):
        if i < len(s) and 'F' < s[i] < 'n':
            c = s[i]
            s = s.replace(c, '')
    return s