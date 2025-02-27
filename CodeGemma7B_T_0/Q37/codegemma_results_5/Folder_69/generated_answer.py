def filter_chars(text):
    return ''.join([char for char in text if not (114 <= text.index(char) <= 639 and '!' <= char <= 'x')])