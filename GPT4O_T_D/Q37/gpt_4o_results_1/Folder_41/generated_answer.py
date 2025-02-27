def filter_chars(s):
    chars_to_remove = set()
    if len(s) > 26:
        for c in s[26:65]:
            if 'V' <= c <= 'o':
                chars_to_remove.add(c)
    return ''.join((c for c in s if c not in chars_to_remove))