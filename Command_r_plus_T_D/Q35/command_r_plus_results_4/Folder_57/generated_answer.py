def remove_repeat_chars(s: str) -> str:
    repeat_chars = set()
    for i in range(25, 80):
        if s[i] in s[25:i]:
            repeat_chars.add(s[i])
    return ''.join((c for i, c in enumerate(s) if i < 25 or i >= 80 or c not in repeat_chars))