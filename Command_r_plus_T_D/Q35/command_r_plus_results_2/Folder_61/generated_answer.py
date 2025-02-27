def remove_repeat_chars(s: str) -> str:
    first_nine_chars = s[:9]
    unique_chars = ''.join(set(first_nine_chars))
    result = []
    for char in s:
        if char in unique_chars:
            result.append(char)
    return ''.join(result)