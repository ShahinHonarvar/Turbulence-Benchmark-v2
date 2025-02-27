def remove_repeat_chars(s: str) -> str:
    unique_chars = set(s[200:203])
    result = []
    for char in s:
        if char in unique_chars:
            continue
        result.append(char)
    return ''.join(result)