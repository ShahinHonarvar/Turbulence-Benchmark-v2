def filter_chars(text):
    result = []
    for i, char in enumerate(text):
        if not (15 <= i <= 55 and 'W' <= char <= '{'):
            result.append(char)
    return ''.join(result)