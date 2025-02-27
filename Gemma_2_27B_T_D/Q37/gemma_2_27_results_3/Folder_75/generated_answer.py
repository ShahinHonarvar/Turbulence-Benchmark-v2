def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 34 <= i <= 67 and 'W' <= char <= 'x':
            continue
        result.append(char)
    return ''.join(result)