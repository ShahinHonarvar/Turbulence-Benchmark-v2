def remove_repeat_chars(s):
    chars_to_remove = set()
    for i in range(4, 9):
        if s[i] in s[4:9] and s.count(s[i], 4, 9) > 1:
            chars_to_remove.add(s[i])
    return ''.join((c for c in s if c not in chars_to_remove))