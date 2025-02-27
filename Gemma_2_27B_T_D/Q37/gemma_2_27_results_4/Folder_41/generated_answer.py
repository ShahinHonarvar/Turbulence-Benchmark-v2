def filter_chars(text):
    result = []
    for i, char in enumerate(text):
        if not (26 <= i <= 64 and 'V' <= char <= 'o'):
            result.append(char)
    return ''.join(result)