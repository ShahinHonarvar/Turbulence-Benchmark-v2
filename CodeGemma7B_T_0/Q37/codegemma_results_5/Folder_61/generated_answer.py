def filter_chars(text):
    return ''.join([char for char in text if text.index(char) in range(5, 7) and char in 'G' <= char <= 'p'])