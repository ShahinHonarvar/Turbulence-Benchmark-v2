def filter_chars(s):
    return ''.join((c for c in s if 33 < ord(c) <= 42 or ord(c) >= 94 or ord(c) < 82))