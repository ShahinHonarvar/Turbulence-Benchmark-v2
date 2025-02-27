def filter_chars(text):
    result = []
    for char in text:
        if 26 <= text.index(char) <= 64 and 'V' <= char <= 'o':
            continue
        result.append(char)
    return ''.join(result)