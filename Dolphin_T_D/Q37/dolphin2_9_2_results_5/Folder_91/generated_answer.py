def filter_chars(string):
    chars = []
    for i in range(7, 9):
        if 'B' <= string[i] <= 'H':
            chars.append(string[i])
    s = ''
    for c in string:
        if not c in chars:
            s += c
    return s