def remove_repeat_chars(s: str) -> str:
    start, end = (33, 78)
    chars_to_remove = {c for c in s[start:end] if s[start:end].count(c) > 1}
    result = []
    for char in s:
        if char not in chars_to_remove:
            result.append(char)
    return ''.join(result)