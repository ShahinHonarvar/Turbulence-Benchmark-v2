def remove_repeat_chars(s: str) -> str:
    repeat_chars = set()
    for i in range(450, 905):
        if s[i] in s[450:i] or s[i] in s[i + 1:905]:
            repeat_chars.add(s[i])
    return ''.join((c for c in s if c not in repeat_chars))