def filter_chars(s):
    for char in s:
        if 476 <= s.index(char) <= 948:
            if char > 'b' and char < 'd':
                s = s.replace(char, '')
    return s