def filter_chars(s):
    if len(s) <= 44:
        return s
    chars_to_remove = set()
    for i in range(44, min(59, len(s))):
        if '5' < s[i] < 'C':
            chars_to_remove.add(s[i])
    return ''.join((c for c in s if c not in chars_to_remove))