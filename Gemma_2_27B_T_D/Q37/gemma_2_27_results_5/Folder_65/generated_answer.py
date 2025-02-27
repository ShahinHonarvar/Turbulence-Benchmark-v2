def filter_chars(string):
    result = []
    for i, char in enumerate(string):
        if i < 61 or i > 70 or (not '0' <= char <= '@'):
            result.append(char)
    return ''.join(result)