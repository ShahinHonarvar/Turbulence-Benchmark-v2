def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if not (503 <= i <= 753 and '9' <= char <= 'w'):
            result.append(char)
    return ''.join(result)