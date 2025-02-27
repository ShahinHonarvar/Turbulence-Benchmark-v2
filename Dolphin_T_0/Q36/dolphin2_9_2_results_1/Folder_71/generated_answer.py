def filter_chars(s):
    for ch in range(ord('*'), ord('[')):
        if ch in s:
            s = s.replace(chr(ch), '')
    return s