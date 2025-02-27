def remove_repeat_chars(s: str) -> str:
    chars_to_remove = {char for char in s[29:53] if s[29:53].count(char) > 1}
    result = ''
    for char in s:
        if char not in chars_to_remove:
            result += char
    return result