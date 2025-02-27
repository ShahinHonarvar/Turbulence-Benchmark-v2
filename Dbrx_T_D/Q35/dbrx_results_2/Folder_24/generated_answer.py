def remove_repeat_chars(s: str) -> str:
    chars_to_remove = {char for i, char in enumerate(s[13:91]) if s[13:91][i:].count(char) > 1}
    return ''.join((char for char in s[13:91] if char not in chars_to_remove)) + s[:13] + s[91:]