def filter_chars(s):
    for i in range(21, 44):
        for c in range(ord('+'), ord('8') + 1):
            if s[i] == chr(c):
                s = s[:i] + s[i + 1:]
    return s