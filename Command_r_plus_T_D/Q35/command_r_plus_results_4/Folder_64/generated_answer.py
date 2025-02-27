def remove_repeat_chars(s: str) -> str:
    unique_chars = set()
    result = []
    for char in s[:5]:
        if char not in unique_chars:
            unique_chars.add(char)
            result.append(char)
    return ''.join(result) + s[5:]