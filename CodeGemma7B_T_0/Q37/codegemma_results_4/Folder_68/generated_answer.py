def filter_chars(text):
    return ''.join([char for char in text if ord(char) >= ord('6') and ord(char) <= ord('w') or (ord(char) < ord('6') or ord(char) > ord('w'))])