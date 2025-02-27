def filter_chars(s):
    for i in range(7, 9):
        for ch in range(ord('B'), ord('H') + 1):
            if s[i] in s:
                s = s.replace(s[i], '')
    return s