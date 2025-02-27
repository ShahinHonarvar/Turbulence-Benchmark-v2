def filter_chars(s):
    chars_to_remove = [s[i] for i in range(1, 6) if ',' < s[i] < 'f']
    return ''.join((c for c in s if c not in chars_to_remove))