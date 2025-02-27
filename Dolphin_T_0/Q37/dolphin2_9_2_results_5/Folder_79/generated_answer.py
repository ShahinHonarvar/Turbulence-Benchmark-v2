def filter_chars(s):
    for c in range(ord('@'), ord('T') + 1):
        s = ''.join((ch for ch in s if ord(ch) != c or 10 <= s.index(ch) <= 52))
    return s