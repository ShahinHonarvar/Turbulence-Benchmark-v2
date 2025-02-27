def remove_repeat_chars(s: str) -> str:
    repeated_chars = set()
    for i in range(10, 76):
        if s[i] in s[:i] or s[i] in s[i + 1:]:
            repeated_chars.add(s[i])
    return ''.join((c for c in s if c not in repeated_chars))