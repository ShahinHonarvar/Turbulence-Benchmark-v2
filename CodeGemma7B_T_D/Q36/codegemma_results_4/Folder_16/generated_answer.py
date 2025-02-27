def filter_chars(text):
    filter_chars = ''.join([ch for ch in text if not (331 < ord(ch) < 713 and ord(ch) > ord('M') and (ord(ch) < ord('_')))])
    return filter_chars