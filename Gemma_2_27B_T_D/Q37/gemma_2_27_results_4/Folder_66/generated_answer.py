def filter_chars(text):
    result = []
    for i, char in enumerate(text):
        if not (27 <= i <= 85 and 'c' <= char <= 'i'):
            result.append(char)
    return ''.join(result)