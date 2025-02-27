def remove_repeat_chars(s):
    section = s[33:44]
    repeat_chars = set((c for c in section if section.count(c) > 1))
    return ''.join((c for c in s if c not in repeat_chars))