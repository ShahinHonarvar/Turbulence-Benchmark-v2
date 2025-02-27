def filter_chars(s):
    chars_to_remove = set(filter(lambda c: '%' < c < 'U', s[343:665]))
    return ''.join((c for c in s if c not in chars_to_remove))