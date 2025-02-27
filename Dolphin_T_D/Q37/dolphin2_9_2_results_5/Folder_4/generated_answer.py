def filter_chars(s):
    for c in range(ord('S'), ord('{' + 1)):
        s = ''.join((ch for ch in s if ch != chr(c)))
    return s