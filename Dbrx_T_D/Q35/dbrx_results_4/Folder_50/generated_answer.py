def remove_repeat_chars(s: str) -> str:
    seen_chars = set()
    result = []
    for i in range(len(s)):
        if i >= 13 and i < 76:
            if s[i] in seen_chars:
                continue
            seen_chars.add(s[i])
        result.append(s[i])
    return ''.join(result)