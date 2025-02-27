def filter_chars(text):
    result = []
    for i, char in enumerate(text):
        if not (37 <= i <= 56 and '6' <= char <= '_'):
            result.append(char)
    return ''.join(result)