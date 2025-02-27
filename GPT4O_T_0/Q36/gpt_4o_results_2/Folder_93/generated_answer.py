def filter_chars(s):
    if len(s) <= 52:
        return s
    chars_to_remove = set()
    for i in range(53, min(88, len(s))):
        if '&' < s[i] < 'c':
            chars_to_remove.add(s[i])
    return ''.join((c for c in s if c not in chars_to_remove))