def filter_chars(text):
    result = []
    for i, char in enumerate(text):
        if not (52 <= i <= 81 and 'A' <= char <= 'U'):
            result.append(char)
    return ''.join(result)