def remove_repeat_chars(s):
    chars_to_remove = set()
    for i in range(10, 76):
        if s[i] in s[:i] or s[i] in s[i + 1:]:
            chars_to_remove.add(s[i])
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s