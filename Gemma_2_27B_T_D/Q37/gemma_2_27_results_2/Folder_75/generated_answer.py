def filter_chars(text):
    result = []
    for i, char in enumerate(text):
        if not (34 <= i <= 67 and 'W' <= char <= 'x'):
            result.append(char)
    return ''.join(result)