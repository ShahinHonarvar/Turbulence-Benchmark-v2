def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if not (61 <= i <= 70 and '0' <= char <= '@'):
            result.append(char)
    return ''.join(result)