def filter_chars(s):
    chars_to_remove = {s[i] for i in range(42, 67) if '6' < s[i] < 'g'}
    return ''.join((c for c in s if c not in chars_to_remove))