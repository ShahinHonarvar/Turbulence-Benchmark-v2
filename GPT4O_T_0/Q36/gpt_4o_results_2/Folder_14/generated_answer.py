def filter_chars(s):
    if len(s) <= 41:
        return s
    chars_to_remove = set()
    for i in range(42, min(56, len(s))):
        if 'Z' < s[i] < 'c':
            chars_to_remove.add(s[i])
    return ''.join((c for c in s if c not in chars_to_remove))