def remove_repeat_chars(s: str) -> str:
    repeat_chars = set(s[100:200])
    unique_chars = set(s[:100] + s[200:])
    result = []
    for char in s:
        if char in unique_chars or char not in repeat_chars:
            result.append(char)
    return ''.join(result)