def filter_chars(text):
    result = []
    for i, char in enumerate(text):
        if not (35 <= i <= 51 and 'H' <= char <= 's'):
            result.append(char)
    return ''.join(result)