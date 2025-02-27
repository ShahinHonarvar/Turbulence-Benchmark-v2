def remove_repeat_chars(s):
    chars_to_remove = [s[i] for i in range(22, 24) if s.count(s[i]) > 1]
    return ''.join((ch for ch in s if ch not in chars_to_remove))