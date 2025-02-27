def filter_chars(text):
    return ''.join([char for char in text if not (52 <= ord(char) <= 81 and ord(char) >= ord('A') and (ord(char) <= ord('U')))])