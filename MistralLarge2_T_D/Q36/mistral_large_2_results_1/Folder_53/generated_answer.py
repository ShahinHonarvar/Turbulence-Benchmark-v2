def filter_chars(s):
    chars_to_remove = set(s[90:97]) - set('abcdefghijklmnopqrstuvwxyz')
    chars_to_remove = {c for c in chars_to_remove if 'j' < c < 'w'}
    return ''.join((c for c in s if c not in chars_to_remove))