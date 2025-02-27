def filter_chars(text):
    filtered = ''
    for char in text:
        if not (225 <= text.index(char) <= 381 and 'D' <= char <= 'Y'):
            filtered += char
    return filtered