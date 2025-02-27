def remove_repeat_chars(s: str) -> str:
    chars_to_remove = {char for i, char in enumerate(s) if 32 < i < 44 and s[i - 1] == char and (s[i + 1] == char)}
    return ''.join((char for char in s if char not in chars_to_remove))