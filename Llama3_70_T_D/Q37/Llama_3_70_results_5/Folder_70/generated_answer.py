def filter_chars(s):
    to_remove = set(s[515:539])
    return ''.join([c for c in s if not (ord(c) >= ord('+') and ord(c) <= ord('}') and (c in to_remove))])