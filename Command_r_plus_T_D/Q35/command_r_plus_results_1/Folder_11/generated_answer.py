def remove_repeat_chars(s: str) -> str:
    to_remove = set()
    for i in range(48, 76):
        if s[i] in s[:i] or s[i] in s[i + 1:]:
            to_remove.add(s[i])
    return ''.join((c for c in s if c not in to_remove))