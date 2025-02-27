def filter_chars(s):
    if len(s) <= 27:
        return s
    filtered_part = s[27:75]
    remove_chars = {c for c in filtered_part if 'A' < c < 'i'}
    return ''.join((c for c in s if c not in remove_chars))