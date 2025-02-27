def filter_chars(s):
    for i in range(32, 47):
        for j in range(ord('0'), ord('k') + 1):
            if chr(j) in s:
                s = s.replace(chr(j), '')
    return s