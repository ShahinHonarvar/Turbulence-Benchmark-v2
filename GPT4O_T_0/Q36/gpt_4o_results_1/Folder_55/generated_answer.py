def filter_chars(s):
    if len(s) <= 4:
        return s
    chars_to_remove = set()
    for i in range(4, min(5, len(s))):
        if 'Y' < s[i] < 's':
            chars_to_remove.add(s[i])
    return ''.join((c for c in s if c not in chars_to_remove))