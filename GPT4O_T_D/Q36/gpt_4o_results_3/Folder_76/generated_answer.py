def filter_chars(s):
    part_to_check = s[670:888]
    chars_to_remove = {c for c in part_to_check if 'B' < c < 'Y'}
    return ''.join((c for c in s if c not in chars_to_remove))