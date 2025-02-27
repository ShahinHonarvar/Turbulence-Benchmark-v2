def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if not (28 <= i <= 65 and 'O' <= char <= 'd'):
            result.append(char)
    return ''.join(result)