def filter_chars(s):
    chars_to_remove = set()
    for c in s[220:403]:
        if '*' < c < '7':
            chars_to_remove.add(c)
    return ''.join((c for c in s if c not in chars_to_remove))