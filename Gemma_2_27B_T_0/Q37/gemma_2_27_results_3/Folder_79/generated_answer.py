def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if not (10 <= i <= 52 and '@' <= char <= 'T'):
            result.append(char)
    return ''.join(result)