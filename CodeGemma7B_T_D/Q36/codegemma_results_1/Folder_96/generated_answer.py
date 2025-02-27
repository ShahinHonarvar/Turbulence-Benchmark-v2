def filter_chars(s):
    return ''.join([ch for ch in s if ord(ch) not in range(38, 81) or ord(ch) <= ord('.') or ord(ch) >= ord('^')])