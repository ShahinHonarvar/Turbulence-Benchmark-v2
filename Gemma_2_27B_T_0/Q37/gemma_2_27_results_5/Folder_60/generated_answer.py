def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if not (12 <= i <= 77 and ':' <= char <= 'L'):
            result.append(char)
    return ''.join(result)