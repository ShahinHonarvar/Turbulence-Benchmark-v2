def filter_chars(s):
    if len(s) < 77:
        return s
    for char in s[52:76]:
        if '5' < char < 'f':
            s = s.replace(char, '')
    return s