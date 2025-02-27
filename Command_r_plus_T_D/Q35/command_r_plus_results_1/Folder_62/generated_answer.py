def remove_repeat_chars(s: str) -> str:
    chars_to_remove = set()
    for i in range(50, 92):
        if s[i] in s[50:92] and s[i] not in chars_to_remove:
            chars_to_remove.add(s[i])
    return ''.join((c for c in s if c not in chars_to_remove))