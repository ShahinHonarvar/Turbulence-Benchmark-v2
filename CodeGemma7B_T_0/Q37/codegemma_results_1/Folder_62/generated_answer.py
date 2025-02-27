def filter_chars(text):
    return ''.join([char for char in text if not (text.index(char) in range(10, 70) and 'I' <= char <= 'K')])