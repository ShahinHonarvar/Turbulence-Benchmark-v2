def filter_chars(text):
    for char in text:
        if 83 <= text.index(char) <= 99 and '*' <= char <= 'j':
            text = text.replace(char, '')
    return text