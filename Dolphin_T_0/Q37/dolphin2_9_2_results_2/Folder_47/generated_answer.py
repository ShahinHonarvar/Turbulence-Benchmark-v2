def filter_chars(s):
    for i in range(38, 55):
        for c in range(ord(':'), ord('r') + 1):
            if s[i] == chr(c):
                s = s[:i] + s[i + 1:]
    return s