def filter_chars(text):
    return ''.join([char for char in text if char not in range(ord('I'), ord('M'), 1) and ord(char) >= 15 and (ord(char) <= 85)])