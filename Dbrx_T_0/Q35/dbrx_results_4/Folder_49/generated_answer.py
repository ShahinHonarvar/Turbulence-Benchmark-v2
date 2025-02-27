def remove_repeat_chars(s: str) -> str:
    char_set = set()
    result = []
    for i in range(len(s)):
        if i >= 90 and i < 200 and (s[i] in char_set):
            continue
        if s[i] not in char_set:
            char_set.add(s[i])
            result.append(s[i])
    return ''.join(result)