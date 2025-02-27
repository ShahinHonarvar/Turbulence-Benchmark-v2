def filter_chars(text):
    for char in text[:]:
        if 38 <= text.index(char) <= 54 and ':' <= char <= 'r':
            text = text.replace(char, '')
    return text