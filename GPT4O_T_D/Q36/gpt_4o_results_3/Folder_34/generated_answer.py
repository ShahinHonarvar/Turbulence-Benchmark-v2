def filter_chars(s):
    if len(s) < 79:
        new_s = s[11:len(s) - 1]
    else:
        new_s = s[11:79]
    chars_to_remove = {c for c in set(new_s) if '?' < c < 'm'}
    return ''.join((c for c in s if c not in chars_to_remove))