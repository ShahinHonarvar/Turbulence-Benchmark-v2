def remove_repeat_chars(s: str) -> str:
    repeat_chars = set()
    for i in range(56, 90):
        if s[i] in s[56:i]:
            repeat_chars.add(s[i])
    return ''.join((c for c in s if c not in repeat_chars))