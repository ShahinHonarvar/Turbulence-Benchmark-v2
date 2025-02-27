def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if not (38 <= i <= 54 and ':' <= char <= 'r'):
            result.append(char)
    return ''.join(result)