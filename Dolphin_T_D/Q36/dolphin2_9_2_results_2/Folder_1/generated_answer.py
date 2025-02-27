def filter_chars(s):
    for char in s:
        if 69 < s.index(char) < 87 and char > '#' and (char < 'L'):
            s = s.replace(char, '')
    return s