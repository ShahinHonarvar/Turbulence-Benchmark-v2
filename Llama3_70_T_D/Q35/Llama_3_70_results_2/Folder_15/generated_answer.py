def remove_repeat_chars(s):
    chars_to_remove = set()
    for c in s[:4]:
        if s[:4].count(c) > 1:
            chars_to_remove.add(c)
    return ''.join((c for c in s if c not in chars_to_remove))