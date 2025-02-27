def filter_chars(s):
    chars_to_remove = {s[i] for i in range(17, 64) if 'O' <= s[i] <= '^'}
    return ''.join((c for c in s if c not in chars_to_remove))