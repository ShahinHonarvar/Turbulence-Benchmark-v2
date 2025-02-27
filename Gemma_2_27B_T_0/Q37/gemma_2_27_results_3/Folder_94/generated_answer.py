def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if not (51 <= i <= 96 and 'X' <= char <= 'p'):
            result.append(char)
    return ''.join(result)