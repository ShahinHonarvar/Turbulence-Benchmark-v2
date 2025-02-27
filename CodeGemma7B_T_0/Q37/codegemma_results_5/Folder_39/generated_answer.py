def filter_chars(text):
    return ''.join([char for char in text if (ord(char) >= ord('A') and ord(char) <= ord('U')) and (text.index(char) >= 52 and text.index(char) <= 81)])