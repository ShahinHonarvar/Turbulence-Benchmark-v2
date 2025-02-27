def filter_chars(s):
    new = [c for c in s if 22 <= s.index(c) <= 43 and '+' <= c <= '8']
    for c in new:
        while c in s:
            s = s.replace(c, '', 1)
    return s