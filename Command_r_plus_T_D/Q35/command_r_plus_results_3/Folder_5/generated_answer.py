def remove_repeat_chars(s: str) -> str:
    chars_to_remove = set()
    for i in range(2, 8):
        if s[i] in s[2:i] and s[i] not in chars_to_remove:
            chars_to_remove.add(s[i])
    result = ''
    for char in s:
        if char not in chars_to_remove:
            result += char
    return result