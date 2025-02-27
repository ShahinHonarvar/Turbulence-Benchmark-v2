def filter_chars(s):
    for char in s:
        if '6' <= char <= 'A' and 138 <= s.index(char) <= 920:
            s = s.replace(char, '')
    return s