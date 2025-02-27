def remove_repeat_chars(s: str) -> str:
    repeat_chars = set(s[462:995])
    unique_chars = set(s[:462] + s[995:])
    result = []
    for char in s:
        if char not in repeat_chars or char in unique_chars:
            result.append(char)
    return ''.join(result)