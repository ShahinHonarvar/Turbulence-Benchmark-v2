def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if not (138 <= i <= 920 and '6' <= char <= 'A'):
            result.append(char)
    return ''.join(result)