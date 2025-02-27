def filter_chars(s):
    chars_to_remove = set([s[i] for i in range(521, 723) if '>' <= s[i] <= '_'])
    return ''.join((c for c in s if c not in chars_to_remove))