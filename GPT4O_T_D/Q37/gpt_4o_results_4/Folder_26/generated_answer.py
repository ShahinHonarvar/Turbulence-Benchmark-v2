def filter_chars(s):
    unwanted = set(s[20:63]).intersection({'i', 'j', 'k'})
    return ''.join((c for c in s if c not in unwanted))