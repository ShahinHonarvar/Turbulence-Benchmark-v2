def remove_repeat_chars(s):
    chars_to_remove = set()
    for i in range(30, 54):
        if s[i] in s[i + 1:54]:
            chars_to_remove.add(s[i])
    return ''.join([c for c in s if c not in chars_to_remove])