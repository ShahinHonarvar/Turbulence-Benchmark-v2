def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if not (27 <= i <= 29 and ';' <= char <= 'b'):
            result.append(char)
    return ''.join(result)