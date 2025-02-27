def filter_chars(s):
    for c in range(ord(':'), ord('r') + 1):
        s = s[:38] + s[38:55].replace(chr(c), '') + s[55:]
    return s