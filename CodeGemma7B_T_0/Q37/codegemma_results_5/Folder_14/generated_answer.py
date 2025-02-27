def filter_chars(text):
    return ''.join([char for char in text if (ord(char) >= ord('A') and ord(char) <= ord('b')) and (ord(char) < 35 or ord(char) > 98)])