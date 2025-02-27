def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if i < 18 or i > 81 or (not 'W' <= char <= '['):
            result.append(char)
    return ''.join(result)