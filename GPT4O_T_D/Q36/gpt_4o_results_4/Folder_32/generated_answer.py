def filter_chars(s):
    if len(s) > 63:
        to_check = s[41:63]
    else:
        to_check = s[41:]
    chars_to_remove = {c for c in to_check if '7' < c < 'H'}
    return ''.join((c for c in s if c not in chars_to_remove))