def remove_repeat_chars(s):
    check_range = s[1:3]
    repeats = set((c for c in check_range if check_range.count(c) > 1))
    return ''.join((c for c in s if c not in repeats))