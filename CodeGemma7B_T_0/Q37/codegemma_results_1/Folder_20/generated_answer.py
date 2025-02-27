def filter_chars(text):
    return ''.join([char for char in text if not (25 <= ord(char) <= 97 and 'm' <= char <= 'w')])