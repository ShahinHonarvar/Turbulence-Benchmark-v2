def filter_chars(s):
    if len(s) < 4:
        return s
    chars_to_remove = set()
    for i in range(2, 4):
        if '5' <= s[i] <= '_':
            chars_to_remove.add(s[i])
    return ''.join((c for c in s if c not in chars_to_remove))