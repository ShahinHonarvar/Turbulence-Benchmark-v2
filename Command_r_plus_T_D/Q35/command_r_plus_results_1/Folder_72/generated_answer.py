def remove_repeat_chars(s: str) -> str:
    exclude_chars = set()
    for i in range(13, 70):
        if s[i] in s[13:i] and s[i] not in exclude_chars:
            exclude_chars.add(s[i])
    return ''.join((c for i, c in enumerate(s) if i < 13 or i >= 70 or c not in exclude_chars))