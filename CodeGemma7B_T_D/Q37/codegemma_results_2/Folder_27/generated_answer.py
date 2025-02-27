def filter_chars(s):
    return ''.join([ch for ch in s if ord(ch) >= ord('=') and ord(ch) <= ord('E')])