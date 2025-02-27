def remove_repeat_chars(s):
    chars_to_remove = set()
    for i in range(10, 79):
        if s[i] in s[:10] or s[i] in s[80:]:
            chars_to_remove.add(s[i])
    s = ''.join([c for c in s if c not in chars_to_remove])
    return s