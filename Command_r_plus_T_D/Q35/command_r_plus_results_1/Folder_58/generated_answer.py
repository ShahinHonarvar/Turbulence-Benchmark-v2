def remove_repeat_chars(s: str) -> str:
    repeat_chars = set()
    for i in range(103, 802):
        if s[i] in s[103:i] or s[i] in s[i + 1:802]:
            repeat_chars.add(s[i])
    return ''.join((c for c in s if c not in repeat_chars))