def filter_chars(s):
    chars_to_remove = {s[i] for i in range(11, 46) if '!' < s[i] < 'A'}
    return ''.join((c for c in s if c not in chars_to_remove))