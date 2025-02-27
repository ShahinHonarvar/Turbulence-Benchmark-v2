def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if i < 7 or i > 8 or (not 'B' <= char <= 'H'):
            result.append(char)
    return ''.join(result)