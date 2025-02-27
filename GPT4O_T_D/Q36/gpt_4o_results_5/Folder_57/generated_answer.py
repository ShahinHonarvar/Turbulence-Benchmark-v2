def filter_chars(s):
    if len(s) <= 70:
        return s
    chars_to_remove = set()
    for i in range(71, 74):
        if 'A' < s[i] < 'U':
            chars_to_remove.add(s[i])
    return ''.join((c for c in s if c not in chars_to_remove))