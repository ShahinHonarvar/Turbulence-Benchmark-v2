def filter_chars(string):
    result = []
    for i, char in enumerate(string):
        if not (138 <= i <= 920 and '6' <= char <= 'A'):
            result.append(char)
    return ''.join(result)