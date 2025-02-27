def filter_chars(s):
    for char in s[3:8]:
        if '?' < char < 'k':
            s = s.replace(char, '')
    return s