def filter_chars(s):
    for c in range(ord(';') + 1, ord('r') - 1):
        s = ''.join((ch for ch in s if ch != chr(c) or (s.index(ch) < 77 or s.index(ch) >= 87)))
    return s