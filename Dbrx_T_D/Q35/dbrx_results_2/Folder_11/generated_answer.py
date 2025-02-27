def remove_repeat_chars(s: str) -> str:
    char_set = set()
    result = []
    for i in range(len(s)):
        if s[i] not in char_set or (48 <= i < 76 and s[i] in char_set):
            result.append(s[i])
        if 48 <= i < 76:
            char_set.add(s[i])
    return ''.join(result)