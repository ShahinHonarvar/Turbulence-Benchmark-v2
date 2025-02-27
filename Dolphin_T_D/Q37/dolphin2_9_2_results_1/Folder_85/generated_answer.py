def filter_chars(s):
    result = ''
    for i, c in enumerate(s):
        if i < 28 or i > 65 or (not 'O' <= c <= 'd'):
            result += c
    return result