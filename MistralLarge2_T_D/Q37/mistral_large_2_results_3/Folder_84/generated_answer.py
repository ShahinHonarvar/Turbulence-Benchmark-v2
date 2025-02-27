def filter_chars(s):
    chars_to_remove = {s[i] for i in range(138, 921) if '6' <= s[i] <= 'A'}
    return ''.join((c for c in s if c not in chars_to_remove))