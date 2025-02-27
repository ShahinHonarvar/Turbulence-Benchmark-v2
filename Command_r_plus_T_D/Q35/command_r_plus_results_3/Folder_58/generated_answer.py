def remove_repeat_chars(s: str) -> str:
    repeat_chars = set()
    for i in range(103, 802):
        if s[i] in s[103:i] and s[i] not in repeat_chars:
            repeat_chars.add(s[i])
    return ''.join((c for c in s if c not in repeat_chars))