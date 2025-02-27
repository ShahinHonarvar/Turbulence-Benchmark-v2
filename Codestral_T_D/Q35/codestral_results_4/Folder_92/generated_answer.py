def remove_repeat_chars(s):
    chars_to_remove = set((s[i] for i in range(3) if s.count(s[i]) > 1))
    return ''.join((ch for ch in s if ch not in chars_to_remove))