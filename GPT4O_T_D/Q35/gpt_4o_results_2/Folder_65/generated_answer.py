def remove_repeat_chars(s):
    sub_string = s[52:76]
    to_remove = set((c for c in sub_string if sub_string.count(c) > 1))
    return ''.join((c for c in s if c not in to_remove or not 52 <= s.index(c) < 76))