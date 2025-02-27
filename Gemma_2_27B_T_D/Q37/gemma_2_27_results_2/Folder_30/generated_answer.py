def filter_chars(text):
    result = []
    for i, char in enumerate(text):
        if 41 <= i <= 64 and 'K' <= char <= ']':
            continue
        result.append(char)
    return ''.join(result)