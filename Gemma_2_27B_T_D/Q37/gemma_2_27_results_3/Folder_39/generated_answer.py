def filter_chars(s):
    result = []
    for i, c in enumerate(s):
        if not (52 <= i <= 81 and 'A' <= c <= 'U'):
            result.append(c)
    return ''.join(result)