def remove_repeat_chars(s):
    chars_to_remove = set()
    for i in range(2, 6):
        if s.count(s[i]) > 1:
            chars_to_remove.add(s[i])
    return ''.join((ch for ch in s if ch not in chars_to_remove))