def filter_chars(s):
    for i in range(4, 14):
        if 7 <= ord(s[i]) <= ord('o'):
            s = s[:i] + s[i + 1:]
    return s