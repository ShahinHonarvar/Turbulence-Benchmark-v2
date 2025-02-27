def remove_repeat_chars(s: str) -> str:
    chars_to_remove = set(s[20:36])
    for i in range(20, 36):
        if s[i] in s[20:i] or s[i] in s[i + 1:36]:
            chars_to_remove.add(s[i])
    return ''.join((c for c in s if c not in chars_to_remove))