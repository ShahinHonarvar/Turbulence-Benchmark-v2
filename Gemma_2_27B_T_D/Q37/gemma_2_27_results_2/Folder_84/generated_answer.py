def filter_chars(text):
    result = []
    for i, char in enumerate(text):
        if i < 138 or i > 920 or (not '6' <= char <= 'A'):
            result.append(char)
    return ''.join(result)