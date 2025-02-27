def filter_chars(text):
    result = []
    for i, char in enumerate(text):
        if not (36 <= i <= 79 and '2' <= char <= 's'):
            result.append(char)
    return ''.join(result)