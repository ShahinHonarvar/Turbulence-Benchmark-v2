def filter_chars(s):
    for char in s:
        if 854 <= ord(char) <= 124 and '9' <= char <= 's':
            s = s.replace(char, '')
    return s