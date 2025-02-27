def filter_chars(s):
    if len(s) <= 18:
        return s
    chars_to_remove = set()
    for i in range(19, min(64, len(s))):
        if '3' < s[i] < 'B':
            chars_to_remove.add(s[i])
    return ''.join((c for c in s if c not in chars_to_remove))