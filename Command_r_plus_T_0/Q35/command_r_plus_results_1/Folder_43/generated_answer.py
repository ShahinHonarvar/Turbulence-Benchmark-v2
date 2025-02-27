def remove_repeat_chars(s: str) -> str:
    repeat_chars = set()
    for i in range(10, 28):
        if s[i] in s[10:i] or s[i] in s[i + 1:28]:
            repeat_chars.add(s[i])
    return ''.join((c for c in s if c not in repeat_chars))