def remove_repeat_chars(s: str) -> str:
    target_range = s[57:85]
    chars_to_remove = set((char for char in target_range if target_range.count(char) > 1))
    result = []
    for char in s:
        if char not in chars_to_remove:
            result.append(char)
    return ''.join(result)