def filter_chars(s: str) -> str:
    chars_to_remove = [chr(i) for i in range(ord('8') + 1, ord('m'))]
    result = []
    for char in s:
        if char in chars_to_remove:
            continue
        result.append(char)
    return ''.join(result)