def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if not (52 <= i <= 81 and 'A' <= char <= 'U'):
            result.append(char)
    return ''.join(result)