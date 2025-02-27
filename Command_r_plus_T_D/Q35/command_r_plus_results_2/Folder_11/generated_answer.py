def remove_repeat_chars(s):
    chars_to_remove = set()
    for i in range(48, 76):
        if s[i] in s[48:i] or s[i] in s[i + 1:76]:
            chars_to_remove.add(s[i])
    return ''.join((c for c in s if c not in chars_to_remove))