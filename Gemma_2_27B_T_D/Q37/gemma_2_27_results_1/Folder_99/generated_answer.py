def filter_chars(s):
    result = []
    for i, c in enumerate(s):
        if i < 373 or i > 901 or c < 'T' or (c > 'h'):
            result.append(c)
    return ''.join(result)