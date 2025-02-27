def filter_chars(text):
    return ''.join([char for char in text if ord(char) not in range(51, 97) or not (ord(char) >= ord('X') and ord(char) <= ord('p'))])