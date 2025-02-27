def filter_chars(text):
    result = []
    for i, char in enumerate(text):
        if not (12 <= i <= 88 and '&' <= char <= 'v'):
            result.append(char)
    return ''.join(result)