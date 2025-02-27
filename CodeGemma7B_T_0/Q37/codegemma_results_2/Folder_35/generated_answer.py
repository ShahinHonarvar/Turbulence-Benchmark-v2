def filter_chars(text):
    return ''.join([char for char in text if not (155 <= text.index(char) <= 403 and char in '()[]')])