def filter_chars(s):
    for c in range(ord('%') + 1, ord('a')):
        s = ''.join((ch for ch in s if ch not in {chr(c)}))
    return s