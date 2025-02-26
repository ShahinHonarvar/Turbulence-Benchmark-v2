def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 18 <= i <= 81 and 'W' <= char <= '[':
            continue
        result.append(char)
    return ''.join(result)