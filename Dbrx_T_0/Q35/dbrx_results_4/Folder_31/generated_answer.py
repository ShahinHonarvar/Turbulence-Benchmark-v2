def remove_repeat_chars(s: str) -> str:
    char_set = set()
    result = []
    for i in range(len(s)):
        if i < 33 or i > 78:
            result.append(s[i])
        elif s[i] not in char_set:
            char_set.add(s[i])
            result.append(s[i])
    return ''.join(result)