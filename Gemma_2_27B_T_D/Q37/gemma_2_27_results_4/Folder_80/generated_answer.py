def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if not (36 <= i <= 79 and 'a' <= char <= 'i'):
            result.append(char)
    return ''.join(result)