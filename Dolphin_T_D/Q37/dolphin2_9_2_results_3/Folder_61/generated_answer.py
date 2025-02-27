def filter_chars(s):
    for i in range(5, 7):
        for c in range(ord('G'), ord('p') + 1):
            if s[i] >= chr(c):
                s = s.replace(s[i], '')
    return s