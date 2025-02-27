def filter_chars(s):
    for ch in range(54, 92):
        if ch > ord('J') and ch < ord('X'):
            s = s.replace(chr(ch), '')
    return s