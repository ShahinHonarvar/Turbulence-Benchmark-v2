def filter_chars(s):
    for i in range(670, 888):
        if i < len(s):
            char = s[i]
            if 'B' < char < 'Y':
                s = s.replace(char, '')
    return s