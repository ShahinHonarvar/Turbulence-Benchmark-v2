def remove_repeat_chars(s):
    segment = s[2:7]
    chars_to_remove = set((c for c in segment if segment.count(c) > 1))
    return ''.join((c for c in s if c not in chars_to_remove))