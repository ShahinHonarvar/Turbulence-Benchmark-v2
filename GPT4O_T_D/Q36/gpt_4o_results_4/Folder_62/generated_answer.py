def filter_chars(s):
    if len(s) <= 63 or len(s) <= 89:
        return s
    strip_start = 63
    strip_end = 89
    target_set = set((chr(i) for i in range(ord('*') + 1, ord('w'))))
    for i in range(strip_start + 1, strip_end):
        if i < len(s) and s[i] in target_set:
            s = s.replace(s[i], '')
    return s