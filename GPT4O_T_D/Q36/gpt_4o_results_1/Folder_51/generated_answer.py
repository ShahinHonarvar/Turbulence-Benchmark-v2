def filter_chars(s):
    check_indices = s[59:81]
    remove_chars = {c for c in check_indices if '5' < c < '>'}
    return ''.join((c for c in s if c not in remove_chars))