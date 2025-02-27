def filter_chars(string):
    result = []
    for i, char in enumerate(string):
        if not (35 <= i <= 89 and 'E' <= char <= 't'):
            result.append(char)
    return ''.join(result)