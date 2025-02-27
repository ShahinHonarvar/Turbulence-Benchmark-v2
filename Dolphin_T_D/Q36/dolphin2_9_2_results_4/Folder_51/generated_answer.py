def filter_chars(s):
    for ch in range(58, 81):
        if ch > ord('5') and ch < ord('>'):
            s = s.replace(chr(ch), '')
    return s