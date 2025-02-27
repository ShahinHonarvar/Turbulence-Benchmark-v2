def remove_repeat_chars(s: str) -> str:
    used_chars = set()
    result = []
    for i in range(len(s)):
        if i < 2 or s[i] not in used_chars or i >= 8:
            result.append(s[i])
            if s[i] not in used_chars:
                used_chars.add(s[i])
    return ''.join(result)