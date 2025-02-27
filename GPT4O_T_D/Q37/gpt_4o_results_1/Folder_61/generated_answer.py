def filter_chars(s):
    chars_to_remove = set()
    if len(s) > 5 and 'G' <= s[5] <= 'p':
        chars_to_remove.add(s[5])
    if len(s) > 6 and 'G' <= s[6] <= 'p':
        chars_to_remove.add(s[6])
    return ''.join((c for c in s if c not in chars_to_remove))