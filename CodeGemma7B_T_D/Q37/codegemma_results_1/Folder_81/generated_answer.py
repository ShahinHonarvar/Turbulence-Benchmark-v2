def filter_chars(text):
    return ''.join([i for i in text if not (19 <= ord(i) <= 92 and ord(i) >= ord('8') and (ord(i) <= ord('m')))])