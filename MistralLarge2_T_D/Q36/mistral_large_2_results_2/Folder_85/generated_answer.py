def filter_chars(s):
    chars_to_remove = {s[i] for i in range(55, 80) if 'S' < s[i] < 's'}
    return ''.join((c for c in s if c not in chars_to_remove))