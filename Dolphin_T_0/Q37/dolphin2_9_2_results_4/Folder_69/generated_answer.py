def filter_chars(s):
    for i in range(114, 640):
        c = s[i]
        if ord(c) >= ord('!') and ord(c) <= ord('x'):
            s = s[:i] + s[i + 1:]
    return s