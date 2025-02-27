def remove_repeat_chars(s: str) -> str:
    char_set = set()
    result = []
    for char in s[:4]:
        if char not in char_set:
            char_set.add(char)
            result.append(char)
    for char in s[4:]:
        if char not in char_set:
            result.append(char)
            char_set.add(char)
    return ''.join(result)