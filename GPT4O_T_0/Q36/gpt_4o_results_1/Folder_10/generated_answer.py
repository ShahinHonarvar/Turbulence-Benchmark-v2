def filter_chars(s):
    if len(s) <= 35:
        return s
    chars_to_remove = set()
    for i in range(36, min(60, len(s))):
        if '!' < s[i] < 'B':
            chars_to_remove.add(s[i])
    return ''.join((c for c in s if c not in chars_to_remove))