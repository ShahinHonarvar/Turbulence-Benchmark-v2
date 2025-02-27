def filter_chars(s):
    if len(s) <= 337:
        return s
    chars_to_remove = set()
    for i in range(319, 337):
        if 'B' < s[i] < 'z':
            chars_to_remove.add(s[i])
    return ''.join((ch for ch in s if ch not in chars_to_remove))