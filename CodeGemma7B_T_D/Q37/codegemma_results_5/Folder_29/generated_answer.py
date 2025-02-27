def filter_chars(text):
    return ''.join([char for char in text if ord(char) < ord('&') or ord(char) > ord('v')])