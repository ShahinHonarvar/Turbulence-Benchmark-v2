def filter_chars(s):
    if len(s) <= 11:
        return s
    chars_to_remove = set()
    for i in range(11, min(15, len(s))):
        if 't' < s[i] < 'v':
            chars_to_remove.add(s[i])
    return ''.join((c for c in s if c not in chars_to_remove))