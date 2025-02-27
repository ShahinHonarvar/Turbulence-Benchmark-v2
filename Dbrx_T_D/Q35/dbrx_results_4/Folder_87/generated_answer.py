def remove_repeat_chars(s: str) -> str:
    char_set = set()
    result = []
    for i, char in enumerate(s):
        if i < 20 or i > 42:
            result.append(char)
        elif char not in char_set:
            char_set.add(char)
            result.append(char)
    return ''.join(result)