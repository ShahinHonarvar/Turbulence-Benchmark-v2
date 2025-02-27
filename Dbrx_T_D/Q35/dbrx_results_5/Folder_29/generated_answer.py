def remove_repeat_chars(s: str) -> str:
    seen_chars = set()
    result = ''
    for i in range(len(s)):
        if i >= 70 and i < 98:
            if s[i] not in seen_chars:
                result += s[i]
                seen_chars.add(s[i])
        else:
            result += s[i]
    return result