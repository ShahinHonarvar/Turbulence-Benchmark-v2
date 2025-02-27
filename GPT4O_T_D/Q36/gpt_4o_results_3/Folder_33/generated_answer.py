def filter_chars(s):
    sub_string = s[300:418]
    chars_to_remove = {c for c in sub_string if '9' < c < 'P'}
    return ''.join((c for c in s if c not in chars_to_remove))