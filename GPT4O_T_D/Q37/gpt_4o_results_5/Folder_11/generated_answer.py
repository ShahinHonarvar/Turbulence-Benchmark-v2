def filter_chars(s):
    if len(s) < 29:
        return s
    chars_to_remove = set()
    for i in range(29, min(98, len(s))):
        if '-' <= s[i] <= 'n':
            chars_to_remove.add(s[i])
    return ''.join((c for c in s if c not in chars_to_remove))