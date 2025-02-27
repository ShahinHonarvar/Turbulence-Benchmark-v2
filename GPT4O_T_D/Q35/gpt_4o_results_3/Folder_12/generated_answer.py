def remove_repeat_chars(s):
    if len(s) < 87:
        return s
    substring = s[17:87]
    repeated_chars = set((ch for ch in substring if substring.count(ch) > 1))
    return ''.join((ch for ch in s if ch not in repeated_chars or s.index(ch) <= 16 or s.index(ch) >= 87))