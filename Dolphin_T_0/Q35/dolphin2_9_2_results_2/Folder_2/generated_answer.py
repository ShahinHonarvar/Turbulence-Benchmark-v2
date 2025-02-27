def remove_repeat_chars(s):
    repeat_chars = set()
    for i in range(72, 93):
        if s[i] in s[i + 1:93]:
            repeat_chars.add(s[i])
    new_s = ''
    for c in s:
        if c not in repeat_chars:
            new_s += c
    return new_s