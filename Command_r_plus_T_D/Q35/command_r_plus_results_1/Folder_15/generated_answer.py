def remove_repeat_chars(s: str) -> str:
    unique_chars = set(s[:4])
    result = []
    for char in s:
        if char not in unique_chars:
            result.append(char)
    return ''.join(result)