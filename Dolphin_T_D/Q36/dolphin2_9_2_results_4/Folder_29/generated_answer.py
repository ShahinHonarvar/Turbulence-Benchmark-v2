def filter_chars(s):
    for ch in range(46, 68):
        if ch > ord('H') and ch < ord('s'):
            s = s.replace(chr(ch), '')
    return s