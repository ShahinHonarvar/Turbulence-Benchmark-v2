def filter_chars(s):
    chars = s[70:74]
    for char in chars:
        if ord('A') < ord(char) < ord('U'):
            s = ''.join((c for c in s if c != char))
    return s