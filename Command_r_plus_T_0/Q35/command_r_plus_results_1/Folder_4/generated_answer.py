def remove_repeat_chars(s: str) -> str:
    chars_to_remove = set()
    for i in range(50, 75):
        if s[i - 1] in s[50:75] and s[i - 1] not in chars_to_remove:
            chars_to_remove.add(s[i - 1])
    return ''.join((c for c in s if c not in chars_to_remove))