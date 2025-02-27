def filter_chars(s):
    for c in range(ord(':'), ord('r') + 1):
        c = chr(c)
        s = s[:38] + s[38:55].replace(c, '') + s[55:]
    return s