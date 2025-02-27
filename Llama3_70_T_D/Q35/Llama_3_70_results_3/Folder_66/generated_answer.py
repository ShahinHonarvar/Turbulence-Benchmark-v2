def remove_repeat_chars(s):
    repeat_chars = set()
    for i in range(11, 76):
        if s.count(s[i]) > 1:
            repeat_chars.add(s[i])
    return ''.join((c for i, c in enumerate(s) if c not in repeat_chars))