def filter_chars(s):
    return ''.join([c for c in s if not 30 < ord(c) <= ord(';') and ord(';') <= ord(c) <= ord('g')])