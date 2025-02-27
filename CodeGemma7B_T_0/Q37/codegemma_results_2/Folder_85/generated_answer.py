def filter_chars(text):
    return ''.join([ch for ch in text if not (28 <= ord(ch) <= 65 and ord(ch) >= ord('O') and (ord(ch) <= ord('d')))])