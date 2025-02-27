def filter_chars(s):
    for i in range(323, 526):
        ch = s[i]
        if ')' < ch < 'O':
            s = s.replace(ch, '')
    return s