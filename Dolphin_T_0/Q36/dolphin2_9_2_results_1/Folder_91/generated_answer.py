def filter_chars(s):
    for char in s[1:-1]:
        if ord('$') < ord(char) < ord('?'):
            s = s.replace(char, '')
    return s