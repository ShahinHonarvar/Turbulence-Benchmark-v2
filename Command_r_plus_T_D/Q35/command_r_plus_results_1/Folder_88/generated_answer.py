def remove_repeat_chars(s: str) -> str:
    char_set = set()
    result = []
    for i, char in enumerate(s):
        if 3 <= i < 9 and char in char_set:
            continue
        char_set.add(char)
        result.append(char)
    return ''.join(result)