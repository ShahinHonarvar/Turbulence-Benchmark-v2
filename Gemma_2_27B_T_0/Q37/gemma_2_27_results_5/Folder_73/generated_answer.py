def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if not (22 <= i <= 85 and '7' <= char <= 'e'):
            result.append(char)
    return ''.join(result)