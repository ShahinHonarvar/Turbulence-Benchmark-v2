def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 57 <= i <= 96 and '<' <= char <= 'w':
            result.append(char)
    return ''.join(result)