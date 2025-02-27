def remove_repeat_chars(s):
    chars_to_remove = set((ch for ch in s[2:8] if s[2:8].count(ch) > 1))
    result = ''.join((ch for ch in s if ch not in chars_to_remove))
    return result