def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if not (29 <= i <= 97 and '-' <= char <= 'n'):
            result.append(char)
    return ''.join(result)