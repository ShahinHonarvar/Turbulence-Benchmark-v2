def remove_repeat_chars(s: str) -> str:
    repeat_chars = set()
    for i in range(11, 76):
        if s[i] in s[11:i]:
            repeat_chars.add(s[i])
    return ''.join((c for c in s if c not in repeat_chars))