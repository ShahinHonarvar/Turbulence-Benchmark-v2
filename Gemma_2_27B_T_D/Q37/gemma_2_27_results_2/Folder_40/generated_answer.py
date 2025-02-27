def filter_chars(s):
    result = []
    for i, c in enumerate(s):
        if i in range(2) and '*' <= c <= 's':
            continue
        result.append(c)
    return ''.join(result)