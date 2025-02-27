def filter_chars(s):
    return ''.join([ch for ch in s if not (24 <= ord(ch) <= 82 and ord(ch) >= ord('5') and (ord(ch) <= ord('<')))])