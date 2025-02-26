def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 373 <= i <= 901 and 'T' <= char <= 'h':
            result.append(char)
    return ''.join(result)