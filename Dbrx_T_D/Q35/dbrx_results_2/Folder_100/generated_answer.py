def remove_repeat_chars(s: str) -> str:
    char_set = set()
    result = []
    for i in range(len(s)):
        if i >= 44 and i < 78 and (s[i] in char_set):
            continue
        if i < 44 or i >= 78:
            result.append(s[i])
        if s[i] not in char_set:
            char_set.add(s[i])
    return ''.join(result)