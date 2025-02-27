def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if not (41 <= i <= 64 and 'K' <= char <= ']'):
            result.append(char)
    return ''.join(result)