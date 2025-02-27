def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if not (19 <= i <= 90 and 'F' <= char <= 'h'):
            result.append(char)
    return ''.join(result)