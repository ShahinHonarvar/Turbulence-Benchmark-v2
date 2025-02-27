def filter_chars(s):
    return ''.join((c for c in s if 32 < ord(c) < 84 or (ord('m') < ord(c) < ord('w') and c not in s[32:83])))