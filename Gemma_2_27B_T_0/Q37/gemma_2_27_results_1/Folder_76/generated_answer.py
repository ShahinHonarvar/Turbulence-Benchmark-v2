def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if not (379 <= i <= 898 and 'M' <= char <= 'v'):
            result.append(char)
    return ''.join(result)