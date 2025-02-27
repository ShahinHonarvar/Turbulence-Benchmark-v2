def remove_repeat_chars(s: str) -> str:
    used_chars = set()
    result = []
    for char in s[1:5]:
        if char not in used_chars:
            used_chars.add(char)
            result.append(char)
    for char in s[:1] + s[5:]:
        result.append(char)
    return ''.join(result)