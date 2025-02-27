def filter_chars(s):
    chars_to_remove = set(s[86:93]).intersection(set([chr(i) for i in range(ord('!'), ord('s') + 1)]))
    return ''.join((c for c in s if c not in chars_to_remove))