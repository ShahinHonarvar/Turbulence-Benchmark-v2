def filter_chars(s):
    chars_to_remove = set(s[521:723])
    valid_chars = set('>_<')
    chars_to_remove = chars_to_remove.intersection(valid_chars)
    return ''.join((c for c in s if c not in chars_to_remove))