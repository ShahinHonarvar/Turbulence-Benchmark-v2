def filter_chars(s):
    for i in range(11, 33):
        for j in range(ord('!'), ord('@') + 1):
            if s[i] == chr(j):
                s = s.replace(s[i], '')
    return s