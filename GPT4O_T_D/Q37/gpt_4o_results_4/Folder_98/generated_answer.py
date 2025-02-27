def filter_chars(s):
    indices = range(8, 10)
    chars_to_remove = {s[i] for i in indices if 'R' <= s[i] <= 't'}
    return ''.join((c for c in s if c not in chars_to_remove))