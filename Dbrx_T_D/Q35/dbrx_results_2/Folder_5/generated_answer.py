def remove_repeat_chars(s: str) -> str:
    used_chars = set()
    result = []
    for i in range(len(s)):
        if i == 2:
            used_chars.clear()
        if i >= 2 and i < 8:
            if s[i] in used_chars:
                continue
            used_chars.add(s[i])
        result.append(s[i])
    return ''.join(result)