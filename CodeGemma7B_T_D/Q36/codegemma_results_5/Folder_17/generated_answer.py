def filter_chars(s):
    return ''.join((c for c in s if not 18 < ord(c) < 95 or (ord(c) > ord('K') and ord(c) < ord('a'))))