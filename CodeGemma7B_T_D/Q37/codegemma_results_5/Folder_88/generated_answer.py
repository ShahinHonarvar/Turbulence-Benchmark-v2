def filter_chars(s):
    return ''.join([c for c in s if not (69 <= ord(c) <= 80 and ord(c) >= ord('@') and (ord(c) <= ord('p')))])