def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if not (11 <= i <= 72 and 'i' <= char <= 'v'):
            result.append(char)
    return ''.join(result)