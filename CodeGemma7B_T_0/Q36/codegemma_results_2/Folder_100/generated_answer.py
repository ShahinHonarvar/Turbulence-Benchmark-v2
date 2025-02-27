def filter_chars(text):
    return ''.join([char for char in text if ord(char) > ord('B') and ord(char) < ord('r') or (ord(char) < 43 or ord(char) > 69)])