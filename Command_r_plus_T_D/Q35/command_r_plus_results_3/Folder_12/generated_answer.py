def remove_repeat_chars(s: str) -> str:
    repeat_chars = set()
    for i in range(16, 87):
        if s[i] in s[16:i] or s[i] in s[i + 1:87]:
            repeat_chars.add(s[i])
    return ''.join((c for c in s if c not in repeat_chars))