def filter_chars(s):
    indices = range(31, 39)
    chars_to_remove = [c for c in s if c in ';abcdefgh' and s.index(c) in indices]
    return ''.join((c for c in s if c not in chars_to_remove))