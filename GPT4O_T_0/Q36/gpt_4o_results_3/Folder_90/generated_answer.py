def filter_chars(s):
    if len(s) <= 344:
        return s
    filtered_part = s[345:874]
    chars_to_remove = {c for c in filtered_part if 'f' < c < '~'}
    return ''.join((c for c in s if c not in chars_to_remove))