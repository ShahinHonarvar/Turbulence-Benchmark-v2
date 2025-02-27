def remove_repeat_chars(s: str) -> str:
    used_chars = set()
    result = []
    for i, char in enumerate(s):
        if 34 < i < 69:
            if char in used_chars:
                continue
            else:
                used_chars.add(char)
        result.append(char)
    return ''.join(result)