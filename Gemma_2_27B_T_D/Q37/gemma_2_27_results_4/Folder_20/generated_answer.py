def filter_chars(text):
    result = []
    for i, char in enumerate(text):
        if 25 <= i <= 97 and 'm' <= char <= 'w':
            text = text.replace(char, '')
        result.append(char)
    return ''.join(result)