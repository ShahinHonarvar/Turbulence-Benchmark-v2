def filter_chars(s):
    for c in [chr(i) for i in range(ord('.'), ord('b') + 1)]:
        s = s[:72] + s[72:95].replace(c, '') + s[95:]
    return s