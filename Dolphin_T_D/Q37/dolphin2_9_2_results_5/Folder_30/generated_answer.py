def filter_chars(s):
    for char in s:
        if 41 <= s.index(char) <= 64 and 'K' <= char <= ']':
            s = s.replace(char, '')
    return s