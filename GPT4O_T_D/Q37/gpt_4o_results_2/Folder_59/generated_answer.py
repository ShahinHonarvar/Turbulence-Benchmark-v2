def filter_chars(s):
    if len(s) > 3:
        chars_to_remove = {c for c in s[2:4] if '5' <= c <= '_'}
        s = ''.join((c for c in s if c not in chars_to_remove))
    return s