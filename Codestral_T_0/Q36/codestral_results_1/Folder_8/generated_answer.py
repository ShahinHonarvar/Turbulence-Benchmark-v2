def filter_chars(s):
    for char in s[82:93]:
        if '!' < char < '*':
            s = s.replace(char, '')
    return s