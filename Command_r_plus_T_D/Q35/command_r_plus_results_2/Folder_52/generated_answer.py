def remove_repeat_chars(s: str) -> str:
    chars_to_remove = set()
    for i in range(38, 81):
        if s[i] in s[38:i] or s[i] in s[i + 1:81]:
            chars_to_remove.add(s[i])
    return ''.join((c for c in s if c not in chars_to_remove))