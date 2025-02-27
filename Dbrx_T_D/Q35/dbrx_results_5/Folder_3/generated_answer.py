def remove_repeat_chars(s: str) -> str:
    char_set = set()
    result = []
    for i in range(len(s)):
        if i < 56 or i >= 88 or s[i] not in char_set:
            result.append(s[i])
        if i >= 56 and i < 88:
            char_set.add(s[i])
    return ''.join(result)