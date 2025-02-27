def filter_chars(s):
    if len(s) <= 11:
        return s
    chars_to_remove = set()
    for c in s[12:46]:
        if '!' < c < 'A':
            chars_to_remove.add(c)
    return ''.join((c for c in s if c not in chars_to_remove))