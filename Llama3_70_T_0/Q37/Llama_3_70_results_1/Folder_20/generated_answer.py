def filter_chars(s):
    chars_to_remove = set((c for c in s if 25 <= ord(c) <= 97 and 'm' <= c <= 'w'))
    return ''.join((c for c in s if c not in chars_to_remove))