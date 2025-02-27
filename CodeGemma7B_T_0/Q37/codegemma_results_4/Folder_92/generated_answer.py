def filter_chars(text):
    return ''.join([char for char in text if not (text.index(char) in range(4, 5) and char >= '7' and (char <= 'o'))])