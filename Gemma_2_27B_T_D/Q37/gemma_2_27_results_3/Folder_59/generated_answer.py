def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if i < 2 or i > 3 or (not '5' <= char <= '_'):
            result.append(char)
    return ''.join(result)