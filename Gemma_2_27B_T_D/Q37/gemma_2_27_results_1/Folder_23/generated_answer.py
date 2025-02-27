def filter_chars(text):
    result = []
    for i, char in enumerate(text):
        if not (51 <= i <= 77 and 'V' <= char <= 'Y'):
            result.append(char)
    return ''.join(result)