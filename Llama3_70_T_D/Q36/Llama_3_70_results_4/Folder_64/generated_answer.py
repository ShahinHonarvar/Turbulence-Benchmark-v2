def filter_chars(s):
    for i in range(1, 7):
        char = s[i]
        if '3' < char < '^':
            s = s.replace(char, '')
    return s