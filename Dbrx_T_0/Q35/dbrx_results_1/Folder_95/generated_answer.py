def remove_repeat_chars(s: str) -> str:
    char_set = set()
    result = []
    for i in range(len(s)):
        if i >= 32 and i < 99:
            if s[i] in char_set:
                continue
            else:
                char_set.add(s[i])
        result.append(s[i])
    return ''.join(result)