def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if not (71 <= i <= 94 and 'K' <= char <= 'a'):
            result.append(char)
    return ''.join(result)