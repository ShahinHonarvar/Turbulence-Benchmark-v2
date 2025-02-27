def remove_repeat_chars(s: str) -> str:
    repeat_chars = set()
    for i in range(33, 78):
        if s[i] in s[:i] or s[i] in s[i + 1:]:
            repeat_chars.add(s[i])
    return ''.join((c for c in s if c not in repeat_chars))