def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if not (12 <= i <= 25 and 'P' <= char <= 'x'):
            result.append(char)
    return ''.join(result)