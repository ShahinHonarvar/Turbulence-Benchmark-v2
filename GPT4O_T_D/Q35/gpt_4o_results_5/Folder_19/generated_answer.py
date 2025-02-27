def remove_repeat_chars(s):
    middle_chars = s[2:4]
    repeated_chars = set((c for c in middle_chars if middle_chars.count(c) > 1))
    return ''.join((c for c in s if c not in repeated_chars))