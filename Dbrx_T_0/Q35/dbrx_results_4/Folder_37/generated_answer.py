def remove_repeat_chars(s: str) -> str:
    char_set = set()
    result = []
    for i in range(len(s)):
        if i == 2:
            char_set = set(s[2:7])
        if s[i] in char_set and i != 2 and (i != 7):
            continue
        result.append(s[i])
    return ''.join(result)