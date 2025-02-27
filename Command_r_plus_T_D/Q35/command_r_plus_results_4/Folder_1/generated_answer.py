def remove_repeat_chars(s: str) -> str:
    chars_to_remove = set()
    for i in range(17, 88):
        if s[i] in s[17:i] or s[i] in s[i + 1:88]:
            chars_to_remove.add(s[i])
    return ''.join((c for c in s if c not in chars_to_remove))