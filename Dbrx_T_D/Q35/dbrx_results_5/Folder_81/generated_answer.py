def remove_repeat_chars(s: str) -> str:
    char_set = set()
    result = []
    for i, char in enumerate(s):
        if i >= 20 and i < 200 and (char in char_set):
            continue
        if i >= 20 and i < 200:
            char_set.add(char)
        result.append(char)
    return ''.join(result)