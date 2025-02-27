def filter_chars(string):
    result = []
    for i, char in enumerate(string):
        if not (71 <= i <= 94 and 'K' <= char <= 'a'):
            result.append(char)
    return ''.join(result)