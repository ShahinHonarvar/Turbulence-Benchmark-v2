def filter_chars(text):
    result = []
    for i, char in enumerate(text):
        if i < 41 or i > 86 or (not 'S' <= char <= 's'):
            result.append(char)
    return ''.join(result)