def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 379 <= i <= 898 and 'M' <= char <= 'v':
            continue
        result.append(char)
    return ''.join(result)