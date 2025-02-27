def filter_chars(text):
    return ''.join([char for char in text if char not in 'WNkcFZ([' and 15 <= text.index(char) <= 55])