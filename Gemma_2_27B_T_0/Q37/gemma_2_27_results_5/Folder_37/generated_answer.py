def filter_chars(s):
    result = []
    for i, char in enumerate(s):
        if not (17 <= i <= 63 and 'O' <= char <= '^'):
            result.append(char)
    return ''.join(result)