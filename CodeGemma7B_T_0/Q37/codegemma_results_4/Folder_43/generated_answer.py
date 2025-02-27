def filter_chars(text):
    return ''.join([char for char in text if not (15 <= text.index(char) <= 55 and 'W' <= char <= '{')])