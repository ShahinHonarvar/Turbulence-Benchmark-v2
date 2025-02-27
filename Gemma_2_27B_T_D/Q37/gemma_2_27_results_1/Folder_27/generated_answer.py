def filter_chars(string):
    result = []
    for i, char in enumerate(string):
        if i < 43 or i > 80 or (not '=' <= char <= 'E'):
            result.append(char)
    return ''.join(result)