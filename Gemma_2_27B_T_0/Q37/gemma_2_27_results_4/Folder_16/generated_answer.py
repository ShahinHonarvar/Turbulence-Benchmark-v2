def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if not (225 <= i <= 381 and 'D' <= char <= 'Y'):
            result.append(char)
    return ''.join(result)