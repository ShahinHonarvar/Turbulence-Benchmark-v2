def filter_chars(s):
    for char in s:
        if 54 <= s.index(char) <= 83 and 'j' <= char <= 'v':
            s = s.replace(char, '')
    return s