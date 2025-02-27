def filter_chars(text):
    return ''.join([ch for ch in text if (ord(ch) >= ord('a') and ord(ch) <= ord('f')) and text.index(ch) not in range(24, 80)])