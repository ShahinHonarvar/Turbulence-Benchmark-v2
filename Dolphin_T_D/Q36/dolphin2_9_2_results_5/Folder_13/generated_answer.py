def filter_chars(s):
    chars = s[323:526]
    for char in chars:
        if ')' < char < 'O':
            s = s.replace(char, '')
    return s