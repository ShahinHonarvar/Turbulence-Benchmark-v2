def filter_chars(text):
    result = []
    for i, char in enumerate(text):
        if not (21 <= i <= 43 and '+' <= char <= '8'):
            result.append(char)
    return ''.join(result)