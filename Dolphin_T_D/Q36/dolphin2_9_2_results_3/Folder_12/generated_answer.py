def filter_chars(s):
    for i in range(32, 84):
        if i > ord('m') and i < ord('w'):
            s = s.replace(chr(i), '')
    return s