def remove_repeat_chars(s):
    chars_to_remove = set()
    for i in range(20, 200):
        if s.count(s[i]) > 1:
            chars_to_remove.add(s[i])
    new_s = ''
    for c in s:
        if c not in chars_to_remove:
            new_s += c
    return new_s