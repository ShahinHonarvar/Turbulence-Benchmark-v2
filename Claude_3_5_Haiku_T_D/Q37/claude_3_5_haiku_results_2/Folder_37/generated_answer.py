def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 17 <= i <= 63 and 'O' <= char <= '^':
            continue
        result.append(char)
    return ''.join(result)