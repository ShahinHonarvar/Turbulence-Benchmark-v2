def filter_chars(s):
    return ''.join([ch for ch in s if not (11 <= ord(ch) <= 32 and ord(ch) >= ord('!') and (ord(ch) <= ord('@')))])