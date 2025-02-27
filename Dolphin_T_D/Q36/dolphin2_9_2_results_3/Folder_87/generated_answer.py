def filter_chars(s):
    for c in range(ord('3'), ord('D') + 1):
        if ord(s) > ord('3') and ord(s) < ord('D'):
            s = s.replace(chr(c), '')
    return s