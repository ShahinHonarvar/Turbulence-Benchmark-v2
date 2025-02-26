def remove_repeat_chars(s):
    middle = s[1:4]
    repeats = set((c for c in middle if middle.count(c) > 1))
    return ''.join((c for c in s if c not in repeats))