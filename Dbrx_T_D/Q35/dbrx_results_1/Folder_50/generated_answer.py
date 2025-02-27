def remove_repeat_chars(s: str) -> str:
    used_chars = set()
    result = []
    for i, char in enumerate(s):
        if 13 < i < 76:
            if char in used_chars:
                continue
            used_chars.add(char)
        result.append(char)
    return ''.join(result)