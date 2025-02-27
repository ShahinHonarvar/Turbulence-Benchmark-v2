def remove_repeat_chars(s):
    if len(s) <= 4:
        return s
    chars_between = s[4:9]
    repeated_chars = set((c for c in chars_between if chars_between.count(c) > 1))
    return ''.join((c for c in s if c not in repeated_chars or s.index(c) >= 9))