def filter_chars(s):
    chars_to_remove = {s[i] for i in range(587, 648) if ',' < s[i] < 'c'}
    return ''.join((c for c in s if c not in chars_to_remove))