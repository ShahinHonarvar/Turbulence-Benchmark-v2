def remove_repeat_chars(s: str) -> str:
    chars_to_remove = {char for char in set(s[125:825]) if s[124:].count(char) > 1}
    result = [char for char in s if char not in chars_to_remove]
    return ''.join(result)