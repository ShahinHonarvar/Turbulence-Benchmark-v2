def filter_chars(s):
    return ''.join([c for c in s if not (22 <= ord(c) <= 85 and ord(c) >= ord('7') and (ord(c) <= ord('e')))])