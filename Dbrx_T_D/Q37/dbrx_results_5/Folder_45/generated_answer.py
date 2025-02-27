def filter_chars(s):
    chars_to_remove = ''.join([chr(i) for i in range(72, 95) if ord('.') <= i <= ord('b')])
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s