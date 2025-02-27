def filter_chars(s):
    remove_chars = [c for c in s[2:4] if '5' <= c <= '_']
    return ''.join((c for c in s if c not in remove_chars))