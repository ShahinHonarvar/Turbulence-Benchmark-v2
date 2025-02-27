def filter_chars(text):
    return ''.join([char for char in text if not 343 <= ord(char) <= 665 or (ord(char) > ord('%') and ord(char) < ord('U'))])