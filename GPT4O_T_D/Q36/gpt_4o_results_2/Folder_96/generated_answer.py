def filter_chars(s):
    remove_set = {c for c in s[39:81] if '.' < c < '^'}
    return ''.join((c for c in s if c not in remove_set))