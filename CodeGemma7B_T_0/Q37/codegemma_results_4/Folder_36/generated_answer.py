def filter_chars(text):
    return ''.join([char for char in text if (ord(char) >= ord(',') and ord(char) <= ord('3')) and (ord(char) < ord('259') or ord(char) > ord('502'))])