def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if not (26 <= i <= 64 and 'V' <= char <= 'o'):
            result.append(char)
    return ''.join(result)