def remove_repeat_chars(s: str) -> str:
    chars_to_remove = set(s[46:91])
    result = []
    for char in s:
        if char not in chars_to_remove or s[46:91].count(char) == 1:
            result.append(char)
    return ''.join(result)