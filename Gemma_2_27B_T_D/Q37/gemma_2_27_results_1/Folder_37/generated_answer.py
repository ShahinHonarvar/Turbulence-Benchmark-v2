def filter_chars(text):
    result = []
    for i, char in enumerate(text):
        if not (17 <= i <= 63 and 'O' <= char <= '^'):
            result.append(char)
    return ''.join(result)