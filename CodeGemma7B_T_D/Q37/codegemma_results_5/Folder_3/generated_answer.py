def filter_chars(text):
    return ''.join([c for c in text if not (37 <= ord(c) <= 56 and ord(c) >= ord('6') and (ord(c) <= ord('_')))])