def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if i < 12 or i > 88 or (not '&' <= char <= 'v'):
            result.append(char)
    return ''.join(result)