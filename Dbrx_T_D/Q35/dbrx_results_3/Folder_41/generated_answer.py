def remove_repeat_chars(s: str) -> str:
    chars_to_remove = {char for idx, char in enumerate(s[3:8]) if s[:3] + s[8:]}.intersection(s[:3] + s[8:])
    return ''.join((char for char in s if char not in chars_to_remove))