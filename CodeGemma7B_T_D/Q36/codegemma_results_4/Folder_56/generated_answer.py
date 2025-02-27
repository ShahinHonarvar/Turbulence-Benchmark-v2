def filter_chars(text):
    return ''.join([char for char in text if ord(char) not in range(32, 51) or (64 < ord(char) <= 90 and ord(char) != ord('/'))])