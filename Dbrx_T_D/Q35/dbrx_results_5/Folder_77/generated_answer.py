def remove_repeat_chars(s: str) -> str:
    chars_to_remove = set(s[355:988:2])
    for char in chars_to_remove:
        if s.count(char) > 1:
            s = ''.join((char if i < 355 or i >= 988 or s[i] != char else '' for i, _ in enumerate(s)))
    return s