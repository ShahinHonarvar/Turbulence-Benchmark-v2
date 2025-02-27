def remove_repeat_chars(s: str) -> str:
    used_chars = set()
    result = []
    for char in s[27:96]:
        if char not in used_chars:
            used_chars.add(char)
            result.append(char)
    for char in s[:27] + s[96:]:
        result.append(char)
    return ''.join(result)