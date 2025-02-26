def remove_repeat_chars(s):
    if len(s) <= 91:
        return s
    segment = s[91:97]
    chars_to_remove = set((c for c in segment if segment.count(c) > 1))
    return ''.join((c for c in s if c not in chars_to_remove))