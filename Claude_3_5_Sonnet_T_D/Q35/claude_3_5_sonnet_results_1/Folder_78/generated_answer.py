def remove_repeat_chars(s):
    chars_to_remove = set()
    for i in range(63, 96):
        if i < len(s) and s[i] in s[63:96]:
            chars_to_remove.add(s[i])
    return ''.join((c for c in s if c not in chars_to_remove))