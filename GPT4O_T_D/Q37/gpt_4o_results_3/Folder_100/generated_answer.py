def filter_chars(s):
    if len(s) < 88:
        return s
    chars_to_remove = set()
    for i in range(88, min(91, len(s))):
        if 'J' <= s[i] <= 'Q':
            chars_to_remove.add(s[i])
    return ''.join((c for c in s if c not in chars_to_remove))