def remove_repeat_chars(s: str) -> str:
    char_set = set()
    result = []
    for i, char in enumerate(s):
        if 36 < i < 85 and char in char_set:
            continue
        result.append(char)
        if 36 < i < 85:
            char_set.add(char)
    return ''.join(result)