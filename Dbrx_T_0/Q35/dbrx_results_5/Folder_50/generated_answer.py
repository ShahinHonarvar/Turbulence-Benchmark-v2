def remove_repeat_chars(s: str) -> str:
    char_set = set()
    result = []
    for i in range(len(s)):
        if i >= 13 and i < 76 and (s[i] in char_set):
            continue
        if i < 13 or i >= 76 or s[i] not in char_set:
            result.append(s[i])
            char_set.add(s[i])
    return ''.join(result)