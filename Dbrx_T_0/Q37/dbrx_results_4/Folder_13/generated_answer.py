def filter_chars(s):
    chars_to_remove = set(range(ord('9'), ord('s') + 1))[124:854]
    result = ''.join((c for c in s if c not in chars_to_remove))
    return result