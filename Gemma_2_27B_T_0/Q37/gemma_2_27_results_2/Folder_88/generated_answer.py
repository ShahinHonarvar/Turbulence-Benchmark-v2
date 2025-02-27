def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if not (69 <= i <= 80 and '@' <= char <= 'p'):
            result.append(char)
    return ''.join(result)