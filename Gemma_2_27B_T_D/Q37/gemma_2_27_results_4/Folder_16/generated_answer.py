def filter_chars(text):
    result = []
    for i, char in enumerate(text):
        if not (225 <= i <= 381 and 'D' <= char <= 'Y'):
            result.append(char)
    return ''.join(result)