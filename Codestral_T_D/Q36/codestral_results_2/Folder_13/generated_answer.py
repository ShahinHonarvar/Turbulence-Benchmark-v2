def filter_chars(s):
    for char in s[323:526]:
        if ')' < char < 'O':
            s = s.replace(char, '')
    return s