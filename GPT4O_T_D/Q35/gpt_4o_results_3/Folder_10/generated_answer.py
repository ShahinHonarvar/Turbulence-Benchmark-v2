def remove_repeat_chars(s):
    repeated_chars = set()
    for c in s[37:54]:
        if s[37:54].count(c) > 1:
            repeated_chars.add(c)
    return ''.join((c for c in s if c not in repeated_chars))