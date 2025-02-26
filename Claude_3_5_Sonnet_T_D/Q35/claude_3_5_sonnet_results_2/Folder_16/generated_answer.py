def remove_repeat_chars(s):
    segment = s[91:97]
    repeat_chars = set((c for c in segment if segment.count(c) > 1))
    return ''.join((c for c in s if c not in repeat_chars))