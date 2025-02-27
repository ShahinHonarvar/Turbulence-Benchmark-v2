def filter_chars(s: str) -> str:
    chars_to_remove = [chr(i) for i in range(171, 195) if i > 33 and i < 125]
    result = []
    for char in s:
        if char in chars_to_remove:
            continue
        result.append(char)
    return ''.join(result)