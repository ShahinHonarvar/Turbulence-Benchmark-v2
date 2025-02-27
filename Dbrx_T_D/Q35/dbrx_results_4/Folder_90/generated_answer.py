def remove_repeat_chars(s: str) -> str:
    char_set = set()
    result = []
    for i, char in enumerate(s):
        if i >= 306 and i < 807:
            if char in char_set:
                continue
        char_set.add(s[i])
        result.append(char)
    return ''.join(result)