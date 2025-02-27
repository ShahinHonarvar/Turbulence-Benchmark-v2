def filter_chars(s):
    if len(s) <= 57:
        return s
    substr = s[57:86]
    chars_to_remove = {c for c in substr if '+' < c < 'w'}
    return ''.join((c for c in s if c not in chars_to_remove))