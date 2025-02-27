def filter_chars(s):
    for c in range(ord('-'), ord('D') + 1):
        s = ''.join((ch for ch in s if ch not in chr(c)))
    return s