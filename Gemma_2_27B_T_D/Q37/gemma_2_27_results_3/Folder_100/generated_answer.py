def filter_chars(text):
    result = []
    for i, char in enumerate(text):
        if 88 <= i <= 90 and 'J' <= char <= 'Q':
            continue
        result.append(char)
    return ''.join(result)