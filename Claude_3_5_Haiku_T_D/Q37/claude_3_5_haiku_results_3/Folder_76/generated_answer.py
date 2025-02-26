def filter_chars(string):
    result = []
    for i, char in enumerate(string):
        if 379 <= i <= 898 and 'M' <= char <= 'v':
            continue
        result.append(char)
    return ''.join(result)