def filter_chars(s):
    chars_to_remove = set([s[i] for i in range(31, 73) if 'M' < s[i] < 'j'])
    return ''.join([c for c in s if c not in chars_to_remove])