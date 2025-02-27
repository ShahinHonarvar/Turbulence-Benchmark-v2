def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if not (18 <= i <= 81 and 'W' <= char <= '['):
            result.append(char)
    return ''.join(result)