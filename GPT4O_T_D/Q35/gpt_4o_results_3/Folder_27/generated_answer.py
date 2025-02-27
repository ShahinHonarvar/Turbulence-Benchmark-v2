def remove_repeat_chars(s):
    substring = s[87:89]
    to_remove = set((c for c in substring if substring.count(c) > 1))
    return ''.join((c for c in s if c not in to_remove))