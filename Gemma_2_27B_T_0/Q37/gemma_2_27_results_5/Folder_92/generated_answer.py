def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if i >= 4 and i <= 4 and ('7' <= char <= 'o'):
            continue
        result.append(char)
    return ''.join(result)