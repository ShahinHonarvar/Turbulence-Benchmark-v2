def filter_chars(s):
    chars = [c for c in s if not (32 < ord(c) < 84 and 'm' < c < 'w')]
    return ''.join(chars)