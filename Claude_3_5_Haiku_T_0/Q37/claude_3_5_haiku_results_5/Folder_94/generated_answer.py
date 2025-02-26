def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 51 <= i <= 96 and 'X' <= char <= 'p':
            continue
        result.append(char)
    return ''.join(result)