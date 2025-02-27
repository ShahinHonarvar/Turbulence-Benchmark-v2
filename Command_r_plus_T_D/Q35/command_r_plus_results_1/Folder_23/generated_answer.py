def remove_repeat_chars(s: str) -> str:
    char_set = set()
    result = []
    for char in s:
        if char in char_set or (20 <= len(result) < 36 and char in result):
            continue
        char_set.add(char)
        result.append(char)
    return ''.join(result)