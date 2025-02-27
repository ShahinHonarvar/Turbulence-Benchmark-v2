def remove_repeat_chars(s: str) -> str:
    repeat_chars = set()
    for i in range(42, 87):
        if s[i] in s[42:i] or s[i] in s[i + 1:87]:
            repeat_chars.add(s[i])
    return ''.join((c for c in s if c not in repeat_chars))