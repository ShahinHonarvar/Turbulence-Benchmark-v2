def filter_chars(s):
    for i in range(90, 97):
        char = s[i]
        if 'j' < char < 'w':
            s = s.replace(char, '')
    return s