def remove_repeat_chars(s):
    chars_to_remove = set()
    for i in range(70, 200):
        if s[i] in s[:70] or s[i] in s[200:]:
            chars_to_remove.add(s[i])
    return ''.join([c for c in s if c not in chars_to_remove])