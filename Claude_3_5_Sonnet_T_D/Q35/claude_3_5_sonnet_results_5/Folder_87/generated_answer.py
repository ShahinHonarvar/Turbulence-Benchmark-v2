def remove_repeat_chars(s):
    substring = s[21:43]
    chars_to_remove = set((c for c in substring if substring.count(c) > 1))
    return ''.join((c for c in s if c not in chars_to_remove))