def filter_chars(s):
    for i in range(ord('@'), ord('T') + 1):
        ch = chr(i)
        if 10 <= s.find(ch) <= 52:
            s = s.replace(ch, '')
    return s