def remove_repeat_chars(s: str) -> str:
    repeat_chars = set(s[81:86])
    result = []
    for char in s:
        if char not in repeat_chars:
            result.append(char)
    return ''.join(result)