def filter_chars(s):
    if len(s) < 7:
        return s
    chars_to_remove = set()
    for i in range(5, 7):
        if 'G' <= s[i] <= 'p':
            chars_to_remove.add(s[i])
    return ''.join((c for c in s if c not in chars_to_remove))