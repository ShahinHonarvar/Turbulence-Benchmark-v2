def remove_repeat_chars(s: str) -> str:
    chars_to_remove = set()
    for i in range(56, 88):
        if s[i] in s[56:88] and s[i] != s[56:88].index(s[i]):
            chars_to_remove.add(s[i])
    return ''.join((c for c in s if c not in chars_to_remove))