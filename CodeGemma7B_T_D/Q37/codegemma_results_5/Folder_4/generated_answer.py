def filter_chars(s):
    return ''.join([c for c in s if not (ord(c) >= ord('S') and ord(c) <= ord('{')) or c not in s[19:34]])