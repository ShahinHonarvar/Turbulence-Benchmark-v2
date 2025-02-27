def filter_chars(s):
    if len(s) < 80:
        return s
    remove_chars = {c for c in s[79:81] if 'S' < c < '['}
    return ''.join((c for c in s if c not in remove_chars))