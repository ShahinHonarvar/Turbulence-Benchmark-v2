def remove_repeat_chars(s):
    chars_to_remove = set()
    for i in range(20, 51):
        if s.count(s[i], 20, 51) > 1:
            chars_to_remove.add(s[i])
    return ''.join((c for c in s if c not in chars_to_remove))