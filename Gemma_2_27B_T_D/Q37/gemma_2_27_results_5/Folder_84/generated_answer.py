def filter_chars(text):
    result = []
    for i, char in enumerate(text):
        if not (138 <= i <= 920 and '6' <= char <= 'A'):
            result.append(char)
    return ''.join(result)