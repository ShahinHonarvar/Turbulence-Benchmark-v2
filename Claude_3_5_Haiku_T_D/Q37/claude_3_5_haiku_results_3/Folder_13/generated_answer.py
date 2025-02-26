def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 124 <= i <= 854 and '9' <= char <= 's':
            continue
        result.append(char)
    return ''.join(result)