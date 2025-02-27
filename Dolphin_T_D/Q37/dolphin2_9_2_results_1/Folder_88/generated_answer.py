def filter_chars(s):
    for c in range(ord('@'), ord('p') + 1):
        for i in range(69, 81):
            if s[i] == chr(c):
                s = s[:i] + s[i + 1:]
    return s