def filter_chars(s):
    chars_to_remove = {s[i] for i in range(343, 665) if '%' < s[i] < 'U'}
    return ''.join([c for c in s if c not in chars_to_remove])