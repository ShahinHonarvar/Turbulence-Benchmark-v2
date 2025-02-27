def filter_chars(s):
    for char in s[38:81]:
        if '.' < char < '^':
            s = s.replace(char, '')
    return s