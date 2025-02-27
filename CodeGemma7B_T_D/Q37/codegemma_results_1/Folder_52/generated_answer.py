def filter_chars(text):
    return ''.join([char for char in text if not (54 <= ord(char) <= 83 and 'j' <= char <= 'v')])