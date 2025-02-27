def remove_repeat_chars(s: str) -> str:
    char_set = set()
    result = []
    for i, char in enumerate(s):
        if 36 <= i < 52:
            if char in char_set:
                continue
            char_set.add(char)
        result.append(char)
    return ''.join(result)