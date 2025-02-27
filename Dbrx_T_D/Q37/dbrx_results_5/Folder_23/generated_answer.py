def filter_chars(s):
    chars_to_remove = set(s[51:78]).intersection(set(range(ord('V'), ord('Y') + 1)))
    result = ''.join((c for c in s if c < 'V' or c > 'Y' or c not in chars_to_remove))
    return result