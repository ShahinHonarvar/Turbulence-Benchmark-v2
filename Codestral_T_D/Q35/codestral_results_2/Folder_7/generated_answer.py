def remove_repeat_chars(s):
    chars_to_remove = []
    for i in range(375, 926):
        if s[i] in s[376:926] and s[i] not in chars_to_remove:
            chars_to_remove.append(s[i])
    return ''.join((c for c in s if c not in chars_to_remove))