def filter_chars(text):
    result = []
    for i, char in enumerate(text):
        if i < 503 or i > 753 or (not '9' <= char <= 'w'):
            result.append(char)
    return ''.join(result)