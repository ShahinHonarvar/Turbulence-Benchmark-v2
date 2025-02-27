def filter_chars(string):
    result = ''
    for i, c in enumerate(string):
        if i < 7 or i > 9 or '6' <= c <= 'w':
            result += c
    return result