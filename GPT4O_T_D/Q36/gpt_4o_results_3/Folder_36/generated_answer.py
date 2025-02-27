def filter_chars(s):
    result = []
    chars_to_remove = set((c for c in s[284:484] if 'l' < c < 't'))
    for c in s:
        if c not in chars_to_remove:
            result.append(c)
    return ''.join(result)