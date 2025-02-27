def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if not (20 <= i <= 62 and 'i' <= char <= 'k'):
            result.append(char)
    return ''.join(result)