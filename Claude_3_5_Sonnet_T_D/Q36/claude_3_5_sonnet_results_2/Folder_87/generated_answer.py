def filter_chars(s):
    remove_chars = [c for c in s[32:61] if '3' < c < 'D']
    return ''.join((c for c in s if c not in remove_chars))