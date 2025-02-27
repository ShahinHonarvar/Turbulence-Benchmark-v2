def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if not (43 <= i <= 80 and '=' <= char <= 'E'):
            result.append(char)
    return ''.join(result)