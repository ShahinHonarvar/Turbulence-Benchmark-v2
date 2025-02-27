def filter_chars(s):
    return ''.join((c for c in s if 53 < ord(c) < 102 or 51 <= s.index(c) <= 76))