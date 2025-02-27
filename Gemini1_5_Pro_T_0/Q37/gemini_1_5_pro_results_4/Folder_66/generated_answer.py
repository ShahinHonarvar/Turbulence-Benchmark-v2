def filter_chars(text):
    result = []
    for i in range(len(text)):
        char = text[i]
        if not (27 <= i <= 85 and 'c' <= char <= 'i'):
            result.append(char)
    return ''.join(result)