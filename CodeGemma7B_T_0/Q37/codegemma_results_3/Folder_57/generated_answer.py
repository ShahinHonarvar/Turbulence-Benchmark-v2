def filter_chars(text):
    return ''.join([ch for ch in text if not (27 <= ord(ch) <= 85 and ord(ch) >= ord('!') and (ord(ch) <= ord('B')))])