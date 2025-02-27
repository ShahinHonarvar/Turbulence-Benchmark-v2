def remove_repeat_chars(s: str) -> str:
    used_chars = set()
    result = []
    for i in range(len(s)):
        if i >= 409 and i < 502:
            if s[i] in used_chars:
                continue
            used_chars.add(s[i])
        result.append(s[i])
    return ''.join(result)