def filter_chars(s):
    if len(s) <= 87:
        return s
    chars_to_remove = set()
    for i in range(87, min(len(s), 93)):
        if 'E' < s[i] < '~':
            chars_to_remove.add(s[i])
    return ''.join((c for c in s if c not in chars_to_remove))