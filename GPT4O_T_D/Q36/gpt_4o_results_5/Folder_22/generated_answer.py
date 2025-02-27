def filter_chars(s):
    if len(s) <= 56 or len(s) < 84:
        return s
    chars_to_remove = set()
    for i in range(56, 84):
        if ';' < s[i] < 'z':
            chars_to_remove.add(s[i])
    return ''.join((c for c in s if c not in chars_to_remove))