def remove_repeat_chars(s: str) -> str:
    chars_to_remove = {char for i, char in enumerate(s) if 45 < i < 91 and s[:i].count(char) > 0}
    return ''.join((char for char in s if char not in chars_to_remove))