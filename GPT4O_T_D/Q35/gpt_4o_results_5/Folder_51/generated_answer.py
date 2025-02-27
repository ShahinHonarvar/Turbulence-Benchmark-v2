def remove_repeat_chars(s):
    sub_str = s[7:9]
    repeat_chars = set((c for c in sub_str if sub_str.count(c) > 1))
    return ''.join((c for c in s if c not in repeat_chars or s.index(c) < 7 or s.index(c) > 9))