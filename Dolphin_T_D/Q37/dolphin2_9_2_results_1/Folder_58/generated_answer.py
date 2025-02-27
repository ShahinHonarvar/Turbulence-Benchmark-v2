def filter_chars(s):
    for c in range(ord('9'), ord('w') + 1):
        for i in range(503, 754):
            s = s[:i] + s[i + 1:] if s[i] == chr(c) else s
    return s