def remove_repeat_chars(s):
    if len(s) < 9:
        return s
    mid_section = s[8:9]
    repeat_chars = set((c for c in mid_section if mid_section.count(c) > 1))
    return ''.join((c for c in s if c not in repeat_chars))