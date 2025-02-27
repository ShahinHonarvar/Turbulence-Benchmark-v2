def remove_repeat_chars(s: str) -> str:
    chars_to_remove = set()
    for i in range(81, 86):
        if s[i] in s[81:86] and s[i] != s[81:86][0]:
            chars_to_remove.add(s[i])
    return ''.join((c for c in s if c not in chars_to_remove))