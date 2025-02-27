def filter_chars(s):
    chars_to_remove = {s[i] for i in range(56, 86) if '+' < s[i] < 'w'}
    return ''.join((c for c in s if c not in chars_to_remove))