def remove_repeat_chars(s: str) -> str:
    chars_to_remove = {char for char in s if s[0:8].count(char) > 1} - set(s[0:8])
    result = ''
    for char in s:
        if char not in chars_to_remove:
            result += char
    return result