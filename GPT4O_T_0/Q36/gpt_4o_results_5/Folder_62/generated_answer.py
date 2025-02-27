def filter_chars(s):
    if len(s) <= 63:
        return s
    chars_to_remove = set()
    for i in range(64, min(89, len(s))):
        if '*' < s[i] < 'w':
            chars_to_remove.add(s[i])
    return ''.join((c for c in s if c not in chars_to_remove))