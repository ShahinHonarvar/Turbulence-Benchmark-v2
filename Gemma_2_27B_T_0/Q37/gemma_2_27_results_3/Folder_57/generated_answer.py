def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if not (27 <= i <= 85 and '!' <= char <= 'B'):
            result.append(char)
    return ''.join(result)