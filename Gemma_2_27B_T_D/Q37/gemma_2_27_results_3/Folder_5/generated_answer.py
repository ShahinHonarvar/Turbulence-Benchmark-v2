def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if 24 <= i <= 82 and '5' <= char <= '<':
            continue
        result.append(char)
    return ''.join(result)