def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 38 <= i <= 99 and 'A' <= char <= 'Q':
            result.append(char)
    for char in result:
        s = s.replace(char, '')
    return s