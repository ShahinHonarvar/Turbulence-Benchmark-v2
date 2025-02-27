def filter_chars(e):
    return ''.join([c for c in e if ord(c) > ord('5') and ord(c) <= ord('A') or not (ord(c) >= 138 and ord(c) <= 920)])