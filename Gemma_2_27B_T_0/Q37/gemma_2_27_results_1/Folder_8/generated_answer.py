def filter_chars(text):
    result = []
    for i, char in enumerate(text):
        if not (41 <= i <= 86 and 'S' <= char <= 's'):
            result.append(char)
    return ''.join(result)