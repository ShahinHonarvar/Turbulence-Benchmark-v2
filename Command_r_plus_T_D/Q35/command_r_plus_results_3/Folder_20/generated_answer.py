def remove_repeat_chars(s: str) -> str:
    chars_to_remove = set()
    for i in range(27, 96):
        char = chr(i)
        if s.count(char) > 1:
            chars_to_remove.add(char)
    result = ''.join((c for c in s if c not in chars_to_remove))
    return result