def filter_chars(s):
    result = []
    for i, c in enumerate(s):
        if not (42 <= i <= 92 and '/' <= c <= 'a'):
            result.append(c)
    return ''.join(result)