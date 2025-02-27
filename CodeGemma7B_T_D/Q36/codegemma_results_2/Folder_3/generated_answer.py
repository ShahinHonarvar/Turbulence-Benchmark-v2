def filter_chars(s):
    return ''.join([ch for ch in s if not (42 < ord(ch) < 78 and ch in '!?')])