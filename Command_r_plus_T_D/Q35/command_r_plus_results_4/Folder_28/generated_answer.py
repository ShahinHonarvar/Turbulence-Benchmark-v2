def remove_repeat_chars(s: str) -> str:
    chars_to_remove = set()
    for i in range(86, 99):
        if s[i] in s[86:99] and s[i] not in chars_to_remove:
            chars_to_remove.add(s[i])
    return ''.join((c for c in s if c not in chars_to_remove))