def remove_repeat_chars(s: str) -> str:
    unique_chars = set(s[:10])
    result = []
    for char in s:
        if char in unique_chars:
            result.append(char)
    return ''.join(result)