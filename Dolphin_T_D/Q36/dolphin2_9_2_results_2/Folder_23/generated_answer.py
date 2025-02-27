def filter_chars(s):
    for ch in range(ord('5'), ord('}')):
        if s[21:25].count(chr(ch)) > 0:
            s = ''.join((c for c in s if c != chr(ch)))
    return s