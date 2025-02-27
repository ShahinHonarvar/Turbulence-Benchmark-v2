def filter_chars(text):
    result = []
    for i, char in enumerate(text):
        if 17 <= i <= 63 and 'O' <= char <= '^':
            text = text.replace(char, '')
        result.append(char)
    return ''.join(result)