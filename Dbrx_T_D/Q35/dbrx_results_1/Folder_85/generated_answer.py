def remove_repeat_chars(s: str) -> str:
    char_set = set()
    result = []
    for i in range(len(s)):
        if s[i] not in char_set or i < 1 or i > 7:
            result.append(s[i])
            char_set.add(s[i])
    return ''.join(result)