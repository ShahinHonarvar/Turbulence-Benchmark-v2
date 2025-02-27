def filter_chars(text):
    return ''.join([char for char in text if not (521 <= text.index(char) <= 722 and '>' <= char <= '_')])