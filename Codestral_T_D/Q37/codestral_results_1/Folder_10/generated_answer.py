def filter_chars(s):
    for c in range(ord('E'), ord('~') + 1):
        s = s[:63] + s[63:85].replace(chr(c), '') + s[85:]
    return s