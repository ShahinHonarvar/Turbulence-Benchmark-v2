def filter_chars(s):
    if len(s) <= 419:
        substr = s[222:419]
    else:
        substr = s[222:420]
    chars_to_remove = {c for c in substr if '-' < c < 'v'}
    return ''.join((c for c in s if c not in chars_to_remove))