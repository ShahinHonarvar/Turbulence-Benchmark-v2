def remove_repeat_chars(s):
    target = s[7:9]
    repeats = set((c for c in target if target.count(c) > 1))
    return ''.join((c for c in s if c not in repeats))