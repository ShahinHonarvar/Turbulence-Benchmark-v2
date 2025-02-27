def remove_repeat_chars(s):
    chars_to_remove = set()
    for i in range(82, 86):
        if s[i] in s[82:86] and s[82:86].count(s[i]) > 1:
            chars_to_remove.add(s[i])
    return ''.join((c for c in s if c not in chars_to_remove))