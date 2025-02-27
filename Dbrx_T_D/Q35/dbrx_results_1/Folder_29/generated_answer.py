def remove_repeat_chars(s: str) -> str:
    char_set = set()
    result = []
    for i in range(len(s)):
        if i >= 70 and i < 98:
            if s[i] not in char_set:
                result.append(s[i])
                char_set.add(s[i])
        else:
            result.append(s[i])
    return ''.join(result)