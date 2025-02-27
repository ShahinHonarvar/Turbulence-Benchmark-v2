def filter_chars(text):
    return ''.join([c for c in text if ord(c) not in range(40, 63) or not (ord(c) > ord('7') and ord(c) < ord('H'))])