def filter_chars(s):
    for c in range(ord('6'), ord('w') + 1):
        for i in range(7, 10):
            if s[i] == chr(c):
                s = s.replace(chr(c), '')
    return s