def filter_chars(s):
    chars_to_remove = set(s[26:65]).intersection(range(ord('V'), ord('o') + 1))
    for c in chars_to_remove:
        s = s.replace(chr(c), '')
    return s