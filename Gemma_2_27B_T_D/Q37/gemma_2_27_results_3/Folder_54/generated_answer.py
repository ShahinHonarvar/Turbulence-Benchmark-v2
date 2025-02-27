def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 46 <= i <= 85 and '-' <= char <= 'X':
            continue
        result.append(char)
    return ''.join(result)