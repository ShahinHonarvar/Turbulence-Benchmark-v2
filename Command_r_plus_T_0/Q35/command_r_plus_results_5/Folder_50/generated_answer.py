def remove_repeat_chars(s: str) -> str:
    repeat_chars = set()
    for i in range(13, 76):
        if s[i] in s[13:i] or s[i] in s[i + 1:76]:
            repeat_chars.add(s[i])
    return ''.join((c for c in s if c not in repeat_chars))