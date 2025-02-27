def filter_chars(string):
    return ''.join([ch for ch in string if ord(ch) < ord('-') or ord(ch) > ord('D') or (ord(ch) >= ord('0') and ord(ch) <= ord('9'))])