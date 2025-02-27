def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if not (46 <= i <= 85 and '-' <= char <= 'X'):
            result.append(char)
    return ''.join(result)