def remove_repeat_chars(s):
    if len(s) < 32:
        return s
    substring = s[33:99]
    chars_to_remove = set((c for c in substring if substring.count(c) > 1))
    result = ''.join((c for c in s if c not in chars_to_remove or s.index(c) < 32 or s.index(c) > 99))
    return result