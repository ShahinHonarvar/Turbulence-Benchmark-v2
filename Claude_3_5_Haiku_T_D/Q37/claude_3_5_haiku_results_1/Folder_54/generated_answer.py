def filter_chars(string):
    result = []
    for i, char in enumerate(string):
        if 46 <= i <= 85 and '-' <= char <= 'X':
            result.append(char)
    return ''.join(result)