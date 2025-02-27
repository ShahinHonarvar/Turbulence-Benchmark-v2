def filter_chars(s):
    return ''.join([c for c in s if not (75 <= ord(c) <= 99 and ord(c) >= ord('8') and (ord(c) <= ord('e')))])