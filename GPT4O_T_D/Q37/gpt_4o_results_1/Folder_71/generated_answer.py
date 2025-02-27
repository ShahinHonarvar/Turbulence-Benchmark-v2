def filter_chars(s):
    indices_to_check = range(32, 47)
    chars_to_remove = {s[i] for i in indices_to_check if '0' <= s[i] <= 'k'}
    return ''.join((c for c in s if c not in chars_to_remove))