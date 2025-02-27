def filter_chars(text):
    return ''.join([ch for ch in text if ord(ch) >= ord('V') and ord(ch) <= ord('o') or (ord(ch) < ord('A') or ord(ch) > ord('z'))])