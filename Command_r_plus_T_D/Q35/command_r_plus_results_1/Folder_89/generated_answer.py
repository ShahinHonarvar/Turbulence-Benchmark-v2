def remove_repeat_chars(s: str) -> str:
    repeat_chars = set(s[55:84])
    result = []
    for char in s:
        if char in repeat_chars:
            continue
        result.append(char)
    return ''.join(result)