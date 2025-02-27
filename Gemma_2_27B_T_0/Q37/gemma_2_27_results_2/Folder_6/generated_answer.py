def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if not (13 <= i <= 28 and 'c' <= char <= 'n'):
            result.append(char)
    return ''.join(result)