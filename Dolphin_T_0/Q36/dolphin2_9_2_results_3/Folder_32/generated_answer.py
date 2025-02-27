def filter_chars(s):
    for char in s[40:63]:
        if char > '7' and char < 'H':
            s = s.replace(char, '')
    return s