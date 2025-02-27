def remove_repeat_chars(s: str) -> str:
    char_set = set()
    result = []
    for i, char in enumerate(s):
        if 330 <= i < 543 and char in char_set:
            continue
        char_set.add(char)
        if i < 330 or 543 <= i:
            result.append(char)
    return ''.join(result)