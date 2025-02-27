def filter_chars(s):
    result = []
    for i, c in enumerate(s):
        if not (73 <= i <= 74 and 'U' <= c <= 'l'):
            result.append(c)
    return ''.join(result)