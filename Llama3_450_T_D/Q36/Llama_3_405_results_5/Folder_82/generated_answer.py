def filter_chars(s):
    chars_to_filter = set([s[i] for i in range(69, 97) if 'V' < s[i] < 'j'])
    return ''.join([c for c in s if c not in chars_to_filter])