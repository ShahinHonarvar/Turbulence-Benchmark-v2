def filter_chars(s):
    chars_to_remove = [s[i] for i in range(61, 88) if '%' < s[i] < 'q']
    return ''.join((c for c in s if c not in chars_to_remove))