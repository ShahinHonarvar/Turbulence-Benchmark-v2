def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if not (35 <= i <= 89 and 'E' <= char <= 't'):
            result.append(char)
    return ''.join(result)