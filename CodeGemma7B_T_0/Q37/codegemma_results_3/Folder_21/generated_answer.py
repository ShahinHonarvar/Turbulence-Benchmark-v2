def filter_chars(text):
    return ''.join([char for char in text if not (603 <= text.index(char) <= 759 and 'Q' <= char <= 'h')])