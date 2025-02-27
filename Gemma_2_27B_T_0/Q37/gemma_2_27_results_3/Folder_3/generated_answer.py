def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if not (37 <= i <= 56 and '6' <= char <= '_'):
            result.append(char)
    return ''.join(result)