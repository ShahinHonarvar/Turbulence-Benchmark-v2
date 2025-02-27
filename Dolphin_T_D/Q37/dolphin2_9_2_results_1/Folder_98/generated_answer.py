def filter_chars(s):
    res = ''
    for i in s:
        if ord(i) >= ord('R') and ord(i) <= ord('t') and (s.index(i) >= 8) and (s.index(i) <= 9):
            continue
        else:
            res += i
    return res