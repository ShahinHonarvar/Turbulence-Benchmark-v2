def filter_chars(s):
    chars_to_remove = set()
    if len(s) > 477:
        for char in s[477:985]:
            if ',' <= char <= 'V':
                chars_to_remove.add(char)
    return ''.join((c for c in s if c not in chars_to_remove))