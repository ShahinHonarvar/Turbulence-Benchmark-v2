def filter_chars(s):
    chars_to_remove = {s[i] for i in range(43, 59) if '5' < s[i] < 'C'}
    return ''.join((c for c in s if c not in chars_to_remove))