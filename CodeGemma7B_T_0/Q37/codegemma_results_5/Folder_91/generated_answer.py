def filter_chars(text):
    return ''.join([char for char in text if ord(char) >= ord('B') and ord(char) <= ord('H') or (ord(char) < ord('7') or ord(char) > ord('8'))])