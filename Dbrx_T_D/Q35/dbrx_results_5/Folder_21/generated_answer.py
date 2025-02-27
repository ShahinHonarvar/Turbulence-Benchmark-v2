def remove_repeat_chars(s: str) -> str:
    used_chars = set()
    result = []
    for i in range(len(s)):
        if i >= 462 and i < 995:
            if s[i] not in used_chars:
                used_chars.add(s[i])
                result.append(s[i])
        else:
            result.append(s[i])
    return ''.join(result)