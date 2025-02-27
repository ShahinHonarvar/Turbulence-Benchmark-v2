def filter_chars(s):
    for char in s[164:707]:
        if 'O' <= char <= '}':
            s = s.replace(char, '')
    return s