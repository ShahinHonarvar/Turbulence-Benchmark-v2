def filter_chars(s):
    chars_to_remove = set(range(ord('-'), ord('X') + 1)).intersection(set(range(ord(s[45]), ord(s[85]) + 1)))
    return ''.join((c for c in s if c not in chars_to_remove))