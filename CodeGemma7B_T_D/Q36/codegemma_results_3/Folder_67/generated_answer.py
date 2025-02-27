def filter_chars(str_arg):
    return ''.join([ch for ch in str_arg if not (ord(ch) >= ord('H') and ord(ch) <= ord('|'))])