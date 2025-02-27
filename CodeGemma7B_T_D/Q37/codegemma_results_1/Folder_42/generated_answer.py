def filter_chars(text):
    result = []
    for i, char in enumerate(text):
        if 73 <= i <= 74 and 'U' <= char <= 'l':
            continue
        result.append(char)
    return ''.join(result)