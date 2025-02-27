def filter_chars(text):
    return ''.join([ch for ch in text if ord(ch) >= ord('@') and ord(ch) <= ord('T') and (ord(ch) < ord('0') or ord(ch) > ord('9'))])