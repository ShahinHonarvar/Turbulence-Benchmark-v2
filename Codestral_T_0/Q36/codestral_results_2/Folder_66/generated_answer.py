def filter_chars(s):
    for char in s[39:87]:
        if '!' < char < '}':
            s = s.replace(char, '')
    return s