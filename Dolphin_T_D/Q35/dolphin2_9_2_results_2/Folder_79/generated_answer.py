def remove_repeat_chars(s):
    chars_to_remove = []
    for i in range(1, 7):
        if s[i] in s[:i] and s[i] not in chars_to_remove:
            chars_to_remove.append(s[i])
    return ''.join((c for c in s if c not in chars_to_remove))