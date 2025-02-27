def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 73 <= i <= 74 and 'U' <= char <= 'l':
            continue
        result.append(char)
    return ''.join(result)