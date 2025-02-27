def remove_repeat_chars(s: str) -> str:
    char_set = set()
    result = []
    for i in range(len(s)):
        if s[i] in char_set and 44 < i < 91:
            continue
        if s[i] not in char_set:
            char_set.add(s[i])
            result.append(s[i])
    return ''.join(result)