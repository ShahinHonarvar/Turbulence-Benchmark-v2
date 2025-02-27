def filter_chars(s):
    new_s = ''
    for i, char in enumerate(s):
        if 12 <= i <= 77 and ':' <= char <= 'L':
            s = s.replace(char, '')
    return s