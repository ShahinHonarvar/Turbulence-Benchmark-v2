def filter_chars(s):
    result = []
    for i, c in enumerate(s):
        if not (46 <= i <= 85 and '-' <= c <= 'X'):
            result.append(c)
    return ''.join(result)