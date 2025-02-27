def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 155 <= i <= 403 and '(' <= char <= '[':
            continue
        result.append(char)
    return ''.join(result)