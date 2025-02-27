def filter_chars(s):
    remove_chars = [c for c in s[331:713] if 77 < ord(c) < 95]
    return ''.join([c for c in s if c not in remove_chars])