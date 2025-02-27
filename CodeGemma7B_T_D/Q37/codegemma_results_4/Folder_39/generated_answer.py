def filter_chars(text):
    text = ''.join([char for char in text if not (52 <= text.index(char) <= 81 and 'A' <= char <= 'U')])
    return text