def remove_repeat_chars(s: str) -> str:
    chars_to_remove = set()
    for char in s[45:48]:
        if s.count(char) > 1:
            chars_to_remove.add(char)
    result = ''
    for char in s:
        if char not in chars_to_remove:
            result += char
    return result