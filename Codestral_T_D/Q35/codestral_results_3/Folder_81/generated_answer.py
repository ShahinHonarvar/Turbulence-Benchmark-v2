def remove_repeat_chars(s):
    chars_to_remove = set()
    for i in range(20, 200):
        if i < len(s) and s.count(s[i], 20, 200) > 1:
            chars_to_remove.add(s[i])
    return ''.join((c for c in s if c not in chars_to_remove))