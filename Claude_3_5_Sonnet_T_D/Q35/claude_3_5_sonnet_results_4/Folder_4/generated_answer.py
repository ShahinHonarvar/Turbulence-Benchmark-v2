def remove_repeat_chars(s):
    chars_to_remove = set()
    for i in range(50, 74):
        if i < len(s) and s[i] in s[50:74]:
            chars_to_remove.add(s[i])
    return ''.join((c for c in s if c not in chars_to_remove))