def filter_chars(s: str) -> str:
    chars_to_remove = [chr(i) for i in range(170, 196) if i > 33 and i < 125]
    result = []
    for char in s:
        if char not in chars_to_remove:
            result.append(char)
    return ''.join(result)