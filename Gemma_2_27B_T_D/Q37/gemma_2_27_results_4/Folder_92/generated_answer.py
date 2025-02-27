def filter_chars(s):
    for i in range(4, 5):
        for c in s:
            if ord(c) >= ord('7') and ord(c) <= ord('o') and (c in s[i:i + 1]):
                s = s.replace(c, '')
    return s