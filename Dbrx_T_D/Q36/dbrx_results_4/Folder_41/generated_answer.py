def filter_chars(s):
    return ''.join((c for c in s if 102 < ord(c) < 123 or 81 > s.index(c) > 89))