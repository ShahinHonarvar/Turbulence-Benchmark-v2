def filter_chars(text):
    result = []
    for i, char in enumerate(text):
        if 27 <= i <= 85 and '!' <= char <= 'B':
            continue
        result.append(char)
    return ''.join(result)