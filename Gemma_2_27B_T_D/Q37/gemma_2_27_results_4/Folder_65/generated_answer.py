def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 61 <= i <= 70 and '0' <= char <= '@':
            continue
        result.append(char)
    return ''.join(result)