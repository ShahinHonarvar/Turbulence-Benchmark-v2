def filter_chars(text):
    return ''.join([char for char in text if ord(char) <= 85 and ord(char) >= 65 and (ord(char) < 52 or ord(char) > 81)])