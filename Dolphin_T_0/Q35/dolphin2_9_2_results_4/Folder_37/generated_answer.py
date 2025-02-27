def remove_repeat_chars(s):
    chars_to_remove = set()
    for i in range(2, 7):
        if s[i] in s[i + 1:i + 8]:
            chars_to_remove.add(s[i])
    return ''.join((c for c in s if c not in chars_to_remove))