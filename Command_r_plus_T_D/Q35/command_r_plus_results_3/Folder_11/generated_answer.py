def remove_repeat_chars(s: str) -> str:
    unique_chars = set()
    result = []
    for char in s:
        if 48 < ord(char) < 76 and char in unique_chars:
            continue
        unique_chars.add(char)
        result.append(char)
    return ''.join(result)