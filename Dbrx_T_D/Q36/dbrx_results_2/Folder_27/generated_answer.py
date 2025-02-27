def filter_chars(s):
    for i in range(48, 75):
        if 55 < i < 95 and chr(i) in s:
            s = s.replace(chr(i), '', 1)
            s = ''.join((c for c in sorted(s) if c in s))
    return s