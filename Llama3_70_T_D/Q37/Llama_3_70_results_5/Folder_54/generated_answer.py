def filter_chars(s):
    chars_to_remove = []
    for i in range(46, 86):
        if '-' <= chr(i) <= 'X':
            chars_to_remove.append(chr(i))
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s