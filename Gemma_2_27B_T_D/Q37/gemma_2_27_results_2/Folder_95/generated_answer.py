def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if not (35 <= i <= 40 and ')' <= char <= 'l'):
            result.append(char)
    return ''.join(result)