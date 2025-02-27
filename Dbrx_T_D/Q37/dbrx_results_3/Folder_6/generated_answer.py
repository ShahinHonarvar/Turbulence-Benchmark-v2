def filter_chars(s):
    chars_to_remove = set(s[13:29]).intersection(range(ord('c'), ord('n') + 1))
    for c in chars_to_remove:
        s = s.replace(chr(c), '')
    return s