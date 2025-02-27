def filter_chars(s):
    k = ord('K')
    a = ord('a')
    return ''.join((c for c in s if not (k <= ord(c) <= a and 71 <= s.find(c) <= 94)))