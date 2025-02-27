def filter_chars(string):
    result = []
    for i, char in enumerate(string):
        if not (51 <= i <= 96 and 'X' <= char <= 'p'):
            result.append(char)
    return ''.join(result)