def remove_repeat_chars(s: str) -> str:
    char_set = set()
    result = []
    for i in range(min(33, len(s)), min(78, len(s))):
        if s[i] not in char_set:
            char_set.add(s[i])
            result.append(s[i])
    for i in range(max(0, 78 - len(s)), 33, -1):
        if s[i] not in char_set:
            char_set.add(s[i])
            result.append(s[i])
    for i in range(len(s)):
        if 33 <= i < 78:
            continue
        if s[i] not in char_set:
            result.append(s[i])
    return ''.join(result)