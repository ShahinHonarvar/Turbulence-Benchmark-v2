def filter_chars(string):
    result = []
    for i, char in enumerate(string):
        if not (124 <= i <= 854 and '9' <= char <= 's'):
            result.append(char)
    return ''.join(result)