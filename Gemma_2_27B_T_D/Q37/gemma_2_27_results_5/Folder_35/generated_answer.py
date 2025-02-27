def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if not (155 <= i <= 403 and '(' <= char <= ']'):
            result.append(char)
    return ''.join(result)