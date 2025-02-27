def remove_repeat_chars(s: str) -> str:
    used_chars = set()
    result = []
    for i, char in enumerate(s):
        if 32 < i < 99:
            if char in used_chars:
                continue
        used_chars.add(char)
        result.append(char)
    return ''.join(result)