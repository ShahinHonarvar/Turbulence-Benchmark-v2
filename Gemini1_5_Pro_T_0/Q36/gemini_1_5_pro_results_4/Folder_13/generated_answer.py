def filter_chars(s):
    for i in range(323, 526):
        if i < len(s) and ')' < s[i] < 'O':
            c = s[i]
            s = s.replace(c, '')
    return s