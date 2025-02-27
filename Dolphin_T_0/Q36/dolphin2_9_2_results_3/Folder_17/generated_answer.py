def filter_chars(s):
    for ch in range(18, 95):
        if ch > ord('K') and ch < ord('a'):
            s = s.replace(chr(ch), '')
    return s