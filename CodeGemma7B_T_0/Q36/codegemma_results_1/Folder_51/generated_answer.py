def filter_chars(text):
    return ''.join([char for char in text if not (58 < ord(char) < 81 and char > '5' and (char < '>'))])