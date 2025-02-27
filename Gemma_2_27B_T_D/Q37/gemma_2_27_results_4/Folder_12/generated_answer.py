def filter_chars(string):
    result = []
    for i, char in enumerate(string):
        if not (19 <= i <= 90 and 'F' <= char <= 'h'):
            result.append(char)
    return ''.join(result)