def filter_chars(text):
    return ''.join([char for char in text if ord(char) < 57 or (ord(char) > 96 and ord(char) < 60)])