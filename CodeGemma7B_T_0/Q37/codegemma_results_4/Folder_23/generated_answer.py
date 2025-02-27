def filter_chars(text):
    return ''.join([char for char in text if (ord(char) >= ord('V') and ord(char) <= ord('Y')) and (text.index(char) >= 51 and text.index(char) <= 77)])