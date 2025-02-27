def filter_chars(s):
    chars_to_remove = set()
    for i in range(3, 8):
        c = s[i]
        if '?' < c < 'k':
            chars_to_remove.add(c)
    return ''.join((c for c in s if c not in chars_to_remove))