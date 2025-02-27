def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if not (24 <= i <= 79 and 'a' <= char <= 'f'):
            result.append(char)
    return ''.join(result)