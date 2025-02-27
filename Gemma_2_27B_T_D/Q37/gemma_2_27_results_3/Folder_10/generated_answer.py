def filter_chars(s):
    result = []
    for i, c in enumerate(s):
        if i < 63 or i > 84 or c < 'E' or (c > '~'):
            result.append(c)
    return ''.join(result)