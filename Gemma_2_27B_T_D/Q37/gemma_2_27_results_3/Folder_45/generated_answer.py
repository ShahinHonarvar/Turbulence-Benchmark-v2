def filter_chars(text):
    result = []
    for char in text:
        if 72 <= ord(char) <= 94 and '.' <= char <= 'b':
            continue
        result.append(char)
    return ''.join(result)