def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 29 <= i <= 79 and 'K' <= char <= 'z':
            continue
        result.append(char)
    return ''.join(result)