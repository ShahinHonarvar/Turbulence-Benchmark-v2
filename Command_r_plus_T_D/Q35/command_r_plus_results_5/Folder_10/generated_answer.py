def remove_repeat_chars(s: str) -> str:
    chars_to_remove = set(s[36:54])
    chars_to_remove = {char for char in chars_to_remove if s.count(char) > 1}
    result = []
    for char in s:
        if char not in chars_to_remove:
            result.append(char)
    return ''.join(result)