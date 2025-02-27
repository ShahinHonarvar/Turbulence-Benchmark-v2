def filter_chars(s):
    chars_to_remove = set()
    if len(s) > 42:
        for c in s[42:93]:
            if '/' <= c <= 'a':
                chars_to_remove.add(c)
    return ''.join((c for c in s if c not in chars_to_remove))