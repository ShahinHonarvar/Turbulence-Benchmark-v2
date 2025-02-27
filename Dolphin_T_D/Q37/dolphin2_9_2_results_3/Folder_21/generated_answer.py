def filter_chars(s):
    for c in range(ord('Q'), ord('h') + 1):
        for i in range(603, 760):
            if s[i] == chr(c):
                s = s[:i] + s[i + 1:]
    return s