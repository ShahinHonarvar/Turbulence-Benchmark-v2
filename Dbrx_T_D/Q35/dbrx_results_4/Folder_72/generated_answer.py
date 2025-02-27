def remove_repeat_chars(s: str) -> str:
    used_chars = set()
    result = []
    for i in range(13, 70):
        if s[i] not in used_chars:
            result.append(s[i])
            used_chars.add(s[i])
    return ''.join(result)