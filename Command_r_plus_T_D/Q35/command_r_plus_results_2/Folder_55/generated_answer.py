def remove_repeat_chars(s: str) -> str:
    repeat_chars = set()
    for i in range(10, 100):
        if s[i] in s[:i] and s[i] not in repeat_chars:
            repeat_chars.add(s[i])
    return ''.join((c for c in s if c not in repeat_chars))