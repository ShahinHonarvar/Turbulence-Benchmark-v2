def remove_repeat_chars(s):
    chars_to_remove = set()
    for i in range(10, 28):
        if s[i] in s[:10] or s[i] in s[28:]:
            chars_to_remove.add(s[i])
    new_s = ''
    for c in s:
        if c not in chars_to_remove:
            new_s += c
    return new_s