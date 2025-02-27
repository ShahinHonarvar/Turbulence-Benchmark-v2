def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 15 <= i <= 55 and 'W' <= char <= '{':
            continue
        result.append(char)
    return ''.join(result)