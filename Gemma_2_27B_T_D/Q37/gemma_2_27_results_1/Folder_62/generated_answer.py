def filter_chars(text):
    result = []
    for i, char in enumerate(text):
        if not (10 <= i <= 69 and 'I' <= char <= 'K'):
            result.append(char)
    return ''.join(result)