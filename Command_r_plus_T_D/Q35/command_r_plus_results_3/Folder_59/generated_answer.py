def remove_repeat_chars(s: str) -> str:
    first_ten_chars = s[:10]
    unique_chars = set(first_ten_chars)
    result = []
    for char in s:
        if char in unique_chars:
            result.append(char)
    return ''.join(result)