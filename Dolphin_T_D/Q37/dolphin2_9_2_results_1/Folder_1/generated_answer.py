def filter_chars(s):
    for c in range(ord('f'), ord('|') + 1):
        for i in range(41, 80):
            s = s[:i] + (s[i] if s[i] not in chr(c) else '') + s[i + 1:]
    return s