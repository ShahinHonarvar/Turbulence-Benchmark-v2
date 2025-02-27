def filter_chars(s):
    for c in range(ord('@'), ord('p') + 1):
        s = s[:69] + s[69:81].replace(chr(c), '') + s[81:]
    return s