def remove_repeat_chars(s: str) -> str:
    seen_chars = set()
    result = []
    for i in range(len(s)):
        if i >= 20 and i < 51:
            if s[i] not in seen_chars:
                seen_chars.add(s[i])
                result.append(s[i])
        else:
            result.append(s[i])
    return ''.join(result)