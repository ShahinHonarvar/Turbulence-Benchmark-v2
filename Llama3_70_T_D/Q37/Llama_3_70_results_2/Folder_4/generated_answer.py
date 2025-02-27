def filter_chars(s):
    to_remove = set(s[19:34]).intersection(['S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']'])
    return ''.join((c for c in s if c not in to_remove))