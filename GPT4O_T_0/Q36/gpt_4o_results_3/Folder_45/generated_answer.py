def filter_chars(s):
    if len(s) <= 81:
        return s
    chars_to_remove = set()
    for i in range(82, 86):
        if i < len(s) and '!' < s[i] < 's':
            chars_to_remove.add(s[i])
    return ''.join((c for c in s if c not in chars_to_remove))