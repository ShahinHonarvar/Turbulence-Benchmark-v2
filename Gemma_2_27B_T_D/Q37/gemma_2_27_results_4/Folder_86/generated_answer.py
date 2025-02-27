def filter_chars(text):
    result = []
    for i, char in enumerate(text):
        if not (164 <= i <= 706 and 'O' <= char <= '}'):
            result.append(char)
    return ''.join(result)