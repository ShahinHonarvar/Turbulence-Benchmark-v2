def filter_chars(s):
    chars_to_remove = set(s[52:82]).intersection(set(range(ord('A'), ord('V'))))
    for c in chars_to_remove:
        s = s.replace(chr(c), '')
    return s