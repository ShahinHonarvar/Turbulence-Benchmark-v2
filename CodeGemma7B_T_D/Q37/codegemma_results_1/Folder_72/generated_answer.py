def filter_chars(str):
    return ''.join([c for c in str if ord(c) >= ord('H') and ord(c) <= ord('s') or (ord(c) < ord('35') or ord(c) > ord('51'))])