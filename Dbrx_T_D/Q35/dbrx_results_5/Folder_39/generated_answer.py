def remove_repeat_chars(s: str) -> str:
    char_set = set()
    result = []
    for i in range(len(s)):
        if i >= 44 and i < 91 and (s[i] in char_set):
            continue
        if i < 44 or i >= 91:
            result.append(s[i])
        char_set.add(s[i])
    return ''.join(result)