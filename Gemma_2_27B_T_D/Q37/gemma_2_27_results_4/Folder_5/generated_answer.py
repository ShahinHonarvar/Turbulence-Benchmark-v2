def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if not (24 <= i <= 82 and '5' <= char <= '<'):
            result.append(char)
    return ''.join(result)