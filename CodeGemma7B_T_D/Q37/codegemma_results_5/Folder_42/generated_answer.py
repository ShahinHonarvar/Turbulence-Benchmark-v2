def filter_chars(text):
    return ''.join([char for char in text if char not in text[73:75] or not 'U' <= char <= 'l'])