def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if not (124 <= i <= 854 and '9' <= char <= 's'):
            result.append(char)
    return ''.join(result)