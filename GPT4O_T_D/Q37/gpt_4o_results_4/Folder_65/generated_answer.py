def filter_chars(s):
    if len(s) >= 71:
        chars_to_remove = set((c for c in s[61:71] if '0' <= c <= '@'))
    else:
        chars_to_remove = set()
    return ''.join((c for c in s if c not in chars_to_remove))