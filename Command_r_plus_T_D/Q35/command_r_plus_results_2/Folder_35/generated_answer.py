def remove_repeat_chars(s: str) -> str:
    chars_to_remove = set()
    for i in range(77, 84):
        if s[i] in s[77:i] + s[i + 1:84]:
            chars_to_remove.add(s[i])
    return ''.join((c for c in s if c not in chars_to_remove))