def filter_chars(s):
    chars_to_remove = set(s[5:7])
    chars_to_remove = {c for c in chars_to_remove if 'G' <= c <= 'p'}
    return ''.join((c for c in s if c not in chars_to_remove))