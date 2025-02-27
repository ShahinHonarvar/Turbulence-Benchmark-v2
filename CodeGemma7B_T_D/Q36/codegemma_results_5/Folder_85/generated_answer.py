def filter_chars(s):
    return ''.join([ch for ch in s if ord(ch) > ord('S') and ord(ch) < ord('s') or (ord(ch) < 55 or ord(ch) >= 80)])