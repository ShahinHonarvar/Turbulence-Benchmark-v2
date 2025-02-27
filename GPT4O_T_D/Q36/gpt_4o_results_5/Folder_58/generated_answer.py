def filter_chars(s):
    if len(s) <= 318:
        return s
    chars_to_remove = set()
    for i in range(319, 337):
        if i < len(s) and 'B' < s[i] < 'z':
            chars_to_remove.add(s[i])
    return ''.join((c for c in s if c not in chars_to_remove))