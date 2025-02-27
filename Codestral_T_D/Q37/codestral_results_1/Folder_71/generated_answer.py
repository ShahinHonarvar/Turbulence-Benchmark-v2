def filter_chars(s):
    for char in range(ord('0'), ord('k') + 1):
        if 32 <= char <= 46:
            s = s.replace(chr(char), '')
    return s