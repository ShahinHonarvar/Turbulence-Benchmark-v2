def remove_repeat_chars(s: str) -> str:
    to_remove = set()
    for i in range(11, 76):
        if s[i] in s[11:i] and s[i] not in to_remove:
            to_remove.add(s[i])
    return ''.join((c for c in s if c not in to_remove))