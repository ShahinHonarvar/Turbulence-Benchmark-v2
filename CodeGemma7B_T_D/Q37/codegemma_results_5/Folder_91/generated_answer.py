def filter_chars(s):
    return ''.join([ch for ch in s if ch not in s[7:9] or (ord(ch) < ord('B') and ord(ch) > ord('H'))])