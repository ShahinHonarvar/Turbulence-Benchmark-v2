def filter_chars(s):
    result = []
    for i, c in enumerate(s):
        if i < 71 or i > 94 or (not 'K' <= c <= 'a'):
            result.append(c)
    return ''.join(result)