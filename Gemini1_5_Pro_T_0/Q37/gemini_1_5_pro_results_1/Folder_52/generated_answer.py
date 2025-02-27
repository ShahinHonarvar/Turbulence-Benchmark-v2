def filter_chars(s):
    result = []
    for i, c in enumerate(s):
        if not (54 <= i <= 83 and 'j' <= c <= 'v'):
            result.append(c)
    return ''.join(result)