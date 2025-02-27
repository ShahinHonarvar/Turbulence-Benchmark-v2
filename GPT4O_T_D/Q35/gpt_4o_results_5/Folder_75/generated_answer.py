def remove_repeat_chars(s):
    if len(s) <= 22:
        return s
    sub_string = s[21:51]
    repeat_chars = set((c for c in sub_string if sub_string.count(c) > 1))
    result = [c for c in s if c not in repeat_chars or not 20 < s.index(c) < 51]
    return ''.join(result)