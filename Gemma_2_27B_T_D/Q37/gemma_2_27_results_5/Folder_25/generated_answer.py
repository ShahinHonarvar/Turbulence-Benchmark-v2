def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if not (31 <= i <= 38 and ';' <= char <= 'g'):
            result.append(char)
    return ''.join(result)