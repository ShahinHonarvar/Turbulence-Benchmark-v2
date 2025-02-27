def filter_chars(s):
    result = ''
    for i, c in enumerate(s):
        if (i < 71 or i > 96) or (c < '_' or c > 'o'):
            result += c
    return result