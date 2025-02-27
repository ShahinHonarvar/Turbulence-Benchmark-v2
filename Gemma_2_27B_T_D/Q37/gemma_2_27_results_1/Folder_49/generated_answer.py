def filter_chars(s):
    result = []
    for i, c in enumerate(s):
        if 42 <= i <= 97 and '*' <= c <= 'b':
            continue
        result.append(c)
    return ''.join(result)