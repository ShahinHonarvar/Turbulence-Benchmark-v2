def remove_repeat_chars(s: str) -> str:
    chars_to_remove = set()
    for i in range(44, 78):
        if s[i] in s[44:78] and s[i] not in chars_to_remove:
            chars_to_remove.add(s[i])
    return ''.join((c for c in s if c not in chars_to_remove))