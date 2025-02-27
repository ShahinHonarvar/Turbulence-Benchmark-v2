def filter_chars(s):
    result = []
    for i, c in enumerate(s):
        if 25 <= i <= 97 and 'm' <= c <= 'w':
            continue
        result.append(c)
    return ''.join(result)