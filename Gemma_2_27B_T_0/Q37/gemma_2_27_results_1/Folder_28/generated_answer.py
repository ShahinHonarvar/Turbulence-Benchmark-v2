def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if not (20 <= i <= 79 and '!' <= char <= 'T'):
            result.append(char)
    return ''.join(result)