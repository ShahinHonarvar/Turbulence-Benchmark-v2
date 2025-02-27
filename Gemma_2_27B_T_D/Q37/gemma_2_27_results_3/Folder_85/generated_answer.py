def filter_chars(text):
    result = []
    for i, char in enumerate(text):
        if 28 <= i <= 65 and 'O' <= char <= 'd':
            if char not in result:
                continue
        result.append(char)
    return ''.join(result)