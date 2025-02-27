def remove_repeat_chars(s):
    chars = s[50:92]
    to_remove = set((c for c in chars if chars.count(c) > 1))
    return ''.join((c for c in s if c not in to_remove))