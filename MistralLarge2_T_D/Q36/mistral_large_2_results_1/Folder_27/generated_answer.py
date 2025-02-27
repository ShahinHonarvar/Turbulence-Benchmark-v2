def filter_chars(s):
    chars_to_remove = {s[i] for i in range(48, 75) if '6' < s[i] < '_'}
    return ''.join((c for c in s if c not in chars_to_remove))