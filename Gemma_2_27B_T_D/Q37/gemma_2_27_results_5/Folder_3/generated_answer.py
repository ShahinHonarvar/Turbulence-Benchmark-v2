def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 37 <= i <= 56 and '6' <= char <= '_':
            continue
        result.append(char)
    return ''.join(result)