def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if not (7 <= i <= 9 and '6' <= char <= 'w'):
            result.append(char)
    return ''.join(result)