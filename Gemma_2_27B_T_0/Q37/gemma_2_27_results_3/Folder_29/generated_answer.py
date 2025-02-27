def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if not (12 <= i <= 88 and '&' <= char <= 'v'):
            result.append(char)
    return ''.join(result)