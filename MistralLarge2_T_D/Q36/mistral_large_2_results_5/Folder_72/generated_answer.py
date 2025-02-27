def filter_chars(s):
    chars_to_remove = {s[i] for i in range(44, 68) if 'W' < s[i] < 'x'}
    return ''.join((c for c in s if c not in chars_to_remove))