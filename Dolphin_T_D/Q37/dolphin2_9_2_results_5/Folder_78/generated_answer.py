def filter_chars(s):
    for c in range(75, 100):
        if ord(s[c]) >= ord('8') and ord(s[c]) <= ord('e'):
            s = s[:c] + s[c + 1:]
    return s