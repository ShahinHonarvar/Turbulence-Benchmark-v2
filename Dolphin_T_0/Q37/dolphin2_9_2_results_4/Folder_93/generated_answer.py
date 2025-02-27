def filter_chars(s):
    for c in range(ord('H'), ord('e') + 1):
        for i in range(38, 70):
            if s[i] == chr(c):
                s = s[:i] + s[i + 1:]
    return s