def filter_chars(s):
    sub_str = s[47:68]
    to_remove = {c for c in sub_str if 'H' < c < 's'}
    return ''.join((c for c in s if c not in to_remove))