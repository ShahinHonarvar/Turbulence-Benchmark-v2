def remove_repeat_chars(s):
    if len(s) <= 11:
        return s
    chars_in_range = s[11:79]
    repeated_chars = set((c for c in chars_in_range if chars_in_range.count(c) > 1))
    result = ''.join((c for c in s if c not in repeated_chars or s.index(c) >= 79 or s.index(c) < 11))
    return result