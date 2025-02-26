def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 26 <= i <= 64 and 'V' <= char <= 'o':
            continue
        result.append(char)
    return ''.join(result)