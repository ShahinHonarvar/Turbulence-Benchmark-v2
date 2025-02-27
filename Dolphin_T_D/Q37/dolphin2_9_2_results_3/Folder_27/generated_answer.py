def filter_chars(s):
    for c in range(ord('='), ord('E') + 1):
        s = ''.join((ch for ch in s if not (43 <= s.index(ch) <= 80 and ord(ch) in range(ord('='), ord('E') + 1))))
    return s